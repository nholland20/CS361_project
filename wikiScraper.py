import requests
import re
from SPARQLWrapper import SPARQLWrapper, JSON
from datetime import datetime
from pprint import pprint

class Node:
    def __init__(self, name, parent_node, img_link):
        self.name = name
        self.parent = parent_node
        self.children = []
        self.image = img_link

    def to_dict(self):
        return {
            "name": self.name,
            "parent": self.parent.name if self.parent else "null",
            "children": [c.to_dict() for c in self.children],
            "image": self.image if self.image else "null"
        }

def replace_chars(text):
    """
    param1 <string>: Text to escape
    Return: param1 escaped and prepped to enter a SPARQL query
    """
    return_word = text.replace(' ', '_')
    return_word = re.escape(return_word)
    return return_word

def get_image(company_name):
    """
    param1 <string>: name of company to get the image for
    Returns <string>: 'null' if image not found. Otherwise, returns .png link
    """
    company_name = company_name.replace(' ', '_')
    url = "http://wangch9.pythonanywhere.com/" + company_name
    response = requests.request("GET", url)
    if response.status_code != 200:
        return 'null'
    return response.text

def get_top_level_parent(sparql, company_name):
    """
    Recursively finds the top level parent of a company's hierarchical structure
    param1 <object>: the SPARQLWrapper object
    param2 <string>: the name of the company to get the parent of
    Returns: The top level company if what is being searched for is a company. Otherwise, returns False
    """
    try:
        sparql.setQuery(f'''
        SELECT ?type ?name
        WHERE {{dbr:{company_name} rdf:type ?type . 
        OPTIONAL {{dbr:{company_name} dbo:parentCompany ?name}}
        }}
        ''')
        sparql.setReturnFormat(JSON)
        gdata = sparql.query().convert()
        if not gdata['results']['bindings']:
            return False
        
        # extract the parent company's name 
        # (use first result only if more than one - dbpedia lists most current parent first)
        for res in gdata['results']['bindings']:
            print(f"res: {res}")
            if 'name' in res:
                url = res['name']['value']
                name = url.rsplit('/', 1)[-1]
                parent_company = replace_chars(name)
                return get_top_level_parent(sparql, parent_company)
            else:
                # determine if found object is looking at a company data type
                type = (res['type']['value']).rsplit('/', 1)[-1]
                if type == 'Company':
                    return company_name

        return False

    except Exception:
        return    

def build_tree(results, visited_nodes, node):
    """
    Recursively builds the relationship tree structure needed for react-d3-tree from the list of parent-child relationships
    param1 <object>: The results object from the get_all_children query
    param2 <set>: The nodes visited.
    param3 <node>: The node to attach children to.
    Returns: N/A
    """
    if len(visited_nodes) == len(results):
        return

    for res in results:
        child = res['child']['value']
        child = child.rsplit('/', 1)[-1]
        child = child.replace('_', ' ')
        parent = res['parent']['value']
        parent = parent.rsplit('/', 1)[-1]
        parent = parent.replace('_', ' ')

        if parent == node.name:
            visited_nodes.add(child)
            img = get_image(child)
            new_node = Node(child, node, img)
            node.children.append(new_node)
            build_tree(results, visited_nodes, new_node)
        else:
            continue
    return

def get_all_children(sparql, company_name, top_node):
    """
    Finds all the children using the top parent company as the starting point
    param1 <object>: the SPARQLWrapper object
    param2 <string>: name of the top parent company of the hierarchical structure (still escaped for querying)
    param3 <node>: Node representing the top parent company
    """
    sparql.setReturnFormat(JSON)
    sparql.setQuery(f'''
        SELECT ?child ?parent
        WHERE 
        {{ 
            ?parent dbo:parentCompany* dbr:{company_name} . 
            ?child dbo:parentCompany ?parent . 
            MINUS {{ 
                ?child dbp:defunct ?defunctCo }}.
            MINUS {{
                ?child dbo:fate ?fateCo
            }}
        }}
    ''')    
    gdata = sparql.queryAndConvert()

    if not gdata['results']['bindings']:
        return
        
    visited = set()
    build_tree(gdata['results']['bindings'], visited, top_node)

def build_relationship_tree(company_name):
    """
    param1: <string> a company name
    returns: A dictionary representing the corporate heirarchy of the provided company_name
    """
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    
    esc_company_name = replace_chars(company_name)
    print(f"Company Name: {company_name}")

    top_parent = get_top_level_parent(sparql, esc_company_name)
    print(f"top_parent: {top_parent}")
    if not top_parent:
        return False

    top_parent_node_name = top_parent.replace('_', ' ')
    top_parent_node_name = top_parent_node_name.replace('\\', '')

    img = get_image(top_parent_node_name)
    top_node = Node(top_parent_node_name, None, img)

    get_all_children(sparql, top_parent, top_node)

    converted = top_node.to_dict()
    pprint(converted)

    return converted


if __name__ == '__main__':
    print(build_relationship_tree('AB_InBev'))