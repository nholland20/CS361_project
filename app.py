from flask import Flask, request
from flask_cors import CORS, cross_origin
from wikiScraper import build_relationship_tree

app = Flask(__name__, static_folder='my-app/build', static_url_path='')
cors = CORS(app)

@app.route('/api', methods=['GET'])
@cross_origin()
def hello():
    return "hello world"

@app.route('/getByCompanyName/<string:company_name>', methods=['GET'])
@cross_origin()
def get_visualization(company_name):
    """
    Parameter: company_name (str): The company name to build the visualization from.
    Returns: The built visualization.
    """
    print(company_name)
    relationship_tree = build_relationship_tree(company_name)
    return relationship_tree

# @app.route('/')
# @cross_origin()
# def serve():
#     return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()