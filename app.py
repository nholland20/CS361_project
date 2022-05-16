from crypt import methods
from flask import Flask, request
from flask_cors import CORS, cross_origin
from wikiScraper import build_relationship_tree
import wikipedia

app = Flask(__name__, static_folder='my-app/build', static_url_path='')
cors = CORS(app)



@app.route('/api', methods=['GET'])
@cross_origin()
def hello():
    return "hello world"

def check_for_disambiguation(company_name):
    # make sure there is a page. If more than one, provide options to choose from.
    options = wikipedia.search(company_name)
    return options

@app.route('/getByCompanyName/<string:company_name>', methods=['GET'])
@cross_origin()
def get_visualization(company_name):
    """
    Parameter: company_name (str): The company name to build the visualization from.
    Returns: The built visualization.
    """
    print(f"Entry point: {company_name}")
    relationship_tree = build_relationship_tree(company_name)
    print(f"relationship tree: {relationship_tree}")
    if not relationship_tree:
        return {'options': check_for_disambiguation(company_name)}
    return {'tree': relationship_tree}


if __name__ == '__main__':
    app.run()