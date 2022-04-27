import wikipedia
import requests
from bs4 import BeautifulSoup
import re
from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3
from datetime import datetime
from pprint import pprint


def replace_chars(text):
    """
    Doc string
    """
    return_word = text
    chars_to_replace = {'.': r'\u002E', '(': r'\u0028', ')': r'\u0029', ' ': "_"}
    for k, v in chars_to_replace.items():
        return_word = return_word.replace(k, v)
    
    return return_word

def get_top_level_parent(sparql, company_name):
    """
    Doc string
    """
    try:
        sparql.setQuery(f'''
        SELECT ?name
        WHERE {{dbr:{company_name} dbo:parentCompany ?name}}
        ''')
        sparql.setReturnFormat(JSON)
        gdata = sparql.query().convert()
        if not gdata['results']['bindings']:
            return company_name
        
        # extract the parent company (use first result only if more than one)
        for res in gdata['results']['bindings']:
            url = res['name']['value']
            name = url.rsplit('/', 1)[-1]
            parent_company = replace_chars(name)
    
        return get_top_level_parent(sparql, parent_company)

    except Exception:
        return    

def get_result(sparql, parent_company):
    sparql.setQuery(f'''
        SELECT ?name
        WHERE {{?name dbo:parentCompany dbr:{parent_company}}}
    ''')
    sparql.setReturnFormat(JSON)
    gdata = sparql.query().convert()
    return gdata

def benchmark(name, x, *args):
    start = datetime.now()
    print(f"Starting {name} at {start}")
    result = x(*args)
    print(f"{name} ran in {datetime.now() - start}s")
    return result

class Node:
    def __init__(self, name, parent_node):
        self.name = name
        self.parent = parent_node
        self.children = []

    def to_dict(self):
        return {
            "name": self.name,
            "parent": self.parent.name if self.parent else "null",
            "children": [c.to_dict() for c in self.children]
        }

def printTree(node, spaces=2):
    print(" " * spaces, node.name)
    for n in node.children:
        printTree(n, spaces * 2)

def build_tree(sparql, parent_company, node):
    """
    Doc string here.
    """

    print("intermediate")
    printTree(node)
    
    try:
        print(f"Parent company in build tree: {parent_company}")
        gdata = benchmark(f"get child companies {parent_company}", get_result, sparql, parent_company)
    except Exception: 
        return       

    if not gdata['results']['bindings']:
        return node

    for res in gdata['results']['bindings']:
        try:
            url = res['name']['value']
            name = url.rsplit('/', 1)[-1]
            UTF_name = replace_chars(name)
            node.children.append(Node(name, node))
        except:
            print("BAD NAME!!!!")
            continue

        build_tree(sparql, UTF_name, node)

def build_relationship_tree(company_name):
    """
    param1: <string> a company name
    returns: A dictionary representing the corporate heirarchy of the provided company_name
    """
    # Using DBPedia - structured wikipedia data
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    
    company_name = replace_chars(company_name)

    # find top level parent
    top_parent = get_top_level_parent(sparql, company_name)
    top_node = Node(top_parent, None)
    print(f"top parent: {top_parent}")
    if not top_parent:
        build_tree(sparql, company_name, top_node)
    else:
        build_tree(sparql, top_parent, top_node)
    print(f"finished tree: {printTree(top_node)}")

    converted = top_node.to_dict()
    pprint(converted)

    return converted


if __name__ == '__main__':
    build_relationship_tree('Kraft_Foods')