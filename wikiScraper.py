import wikipedia
import requests
from bs4 import BeautifulSoup
import re
from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, N3


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


def build_tree(sparql, parent_company, relationship_tree):
    """
    Doc string here.
    """

    try:
        print(f"Parent company in build tree: {parent_company}")
        sparql.setQuery(f'''
            SELECT ?name
            WHERE {{?name dbo:parentCompany dbr:{parent_company}}}
        ''')
        sparql.setReturnFormat(JSON)
        gdata = sparql.query().convert()
        if not gdata['results']['bindings']:
            return relationship_tree

        for res in gdata['results']['bindings']:
            url = res['name']['value']
            name = url.rsplit('/', 1)[-1]
            UTF_name = replace_chars(name)
            if parent_company in relationship_tree:
                relationship_tree[parent_company].append(name)
            else:
                relationship_tree[parent_company] = [name]
            build_tree(sparql, UTF_name, relationship_tree)
        
        return relationship_tree

    except Exception: 
        return    

def build_relationship_tree(company_name):
    """
    param1: <string> a company name
    returns: A dictionary representing the corporate heirarchy of the provided company_name
    """
    relationship_tree = {}
    # Using DBPedia - structured wikipedia data
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    
    company_name = replace_chars(company_name)

    # find top level parent
    top_parent = get_top_level_parent(sparql, company_name)
    print(f"top parent: {top_parent}")
    if not top_parent:
        finished_tree = build_tree(sparql, company_name, relationship_tree)
    else:
        finished_tree = build_tree(sparql, top_parent, relationship_tree)
    print(f"finished tree: {finished_tree}")

    return finished_tree


if __name__ == '__main__':
    build_relationship_tree('Alphabet Inc.')