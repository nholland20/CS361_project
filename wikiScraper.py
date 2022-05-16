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
    Doc string
    """
    return_word = text.replace(' ', '_')
    return_word = re.escape(return_word)
    # print(f"return word: {return_word}")
    return return_word

def get_image(company_name):
    """
    param1 <string>: name of company to get the image for
    """
    company_name = company_name.replace(' ', '_')
    url = "http://wangch9.pythonanywhere.com/" + company_name
    response = requests.request("GET", url)
    return response.text

def get_top_level_parent(sparql, company_name):
    """
    Doc string
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
        
        # extract the parent company (use first result only if more than one)
        for res in gdata['results']['bindings']:
            print(f"res: {res}")
            if 'name' in res:
                url = res['name']['value']
                name = url.rsplit('/', 1)[-1]
                parent_company = replace_chars(name)
                return get_top_level_parent(sparql, parent_company)
            else:
                type = (res['type']['value']).rsplit('/', 1)[-1]
                if type == 'Company':
                    return company_name

        return False

    except Exception:
        return    

def build_tree(results, visited_nodes, node):
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
        # print(f"child: {child}, parent: {parent}")
    return

def benchmark(name, x, *args):
    start = datetime.now()
    print(f"Starting {name} at {start}")
    result = x(*args)
    print(f"{name} ran in {datetime.now() - start}s")
    return result

def printTree(node, spaces=2):
    print(" " * spaces, node.name)
    for n in node.children:
        printTree(n, spaces * 2)

def get_all_children(sparql, company_name, top_node):
    # Using DBPedia - structured wikipedia data
    sparql.setReturnFormat(JSON)
    sparql.setQuery(f'''
        SELECT ?child ?parent
        WHERE {{ ?parent dbo:parentCompany* dbr:{company_name} . ?child dbo:parentCompany ?parent  }}
    ''')    
    gdata = sparql.queryAndConvert()
    # print(gdata)

    if not gdata['results']['bindings']:
        return

    visited = set()
    build_tree(gdata['results']['bindings'], visited, top_node)

def build_relationship_tree(company_name):
    """
    param1: <string> a company name
    returns: A dictionary representing the corporate heirarchy of the provided company_name
    """
    # Using DBPedia - structured wikipedia data
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    
    esc_company_name = replace_chars(company_name)
    print(f"Company Name: {company_name}")

    # find top level parent. Returns None if already at top.
    top_parent = get_top_level_parent(sparql, esc_company_name)
    print(f"top_parent: {top_parent}")
    if not top_parent:
        return False
    top_parent_node_name = top_parent.replace('_', ' ')
    top_parent_node_name = top_parent_node_name.replace('\\', '')
    img = get_image(top_parent_node_name)
    top_node = Node(top_parent_node_name, None, img)
    print(f"top parent: {top_parent}")

    # If top_level_parent is the same as company_name, ensure looking up a public_company before proceeding
    get_all_children(sparql, top_parent, top_node)

    #print(f"finished tree: {printTree(top_node)}")

    converted = top_node.to_dict()
    pprint(converted)

    return converted


if __name__ == '__main__':
    print(build_relationship_tree('Kraft_Foods'))