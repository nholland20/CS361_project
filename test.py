from SPARQLWrapper import SPARQLWrapper, JSON, N3, JSONLD
from pprint import pprint
import wikipedia

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

def build_tree(results, visited_nodes, node):
    if len(visited_nodes) == len(results):
        return

    for res in results:
        child = res['child']['value']
        child = child.rsplit('/', 1)[-1]
        parent = res['parent']['value']
        parent = parent.rsplit('/', 1)[-1]

        if parent == node.name:
            visited_nodes.add(child)
            new_node = Node(child, node)
            node.children.append(new_node)
            build_tree(results, visited_nodes, new_node)
        else:
            continue
        # print(f"child: {child}, parent: {parent}")
    return

def get_all_children(company_name):
    # Using DBPedia - structured wikipedia data
    sparql = SPARQLWrapper('https://dbpedia.org/sparql')
    sparql.setReturnFormat(JSON)
    sparql.setQuery(f'''
        SELECT ?child ?parent
        WHERE {{ ?parent dbo:parentCompany* dbr:{company_name} . ?child dbo:parentCompany ?parent  }}
    ''')    
    gdata = sparql.queryAndConvert()
    # print(gdata)
    top_node = Node(company_name, None)

    if not gdata['results']['bindings']:
        return

    visited = set()
    build_tree(gdata['results']['bindings'], visited, top_node)
    
    converted_tree = top_node.to_dict()
    pprint(converted_tree)

    return converted_tree

def check_for_disambiguation(company_name):
    # make sure there is a page. If more than one, provide options to choose from.
    wikiContent = wikipedia.search(company_name)
    print(wikiContent)

if __name__ == '__main__':
   check_for_disambiguation("Apple")

