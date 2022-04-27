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
    # relationship_tree = build_relationship_tree(company_name)
    return ({
        "name": "Microsoft",
        "parent": "null",
        "children": [
        {
            "name": "MSN_TV",
            "parent": "Microsoft",
            "children": [],
        },
        {
            "name": "Access_Software",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Massive_Incorporated",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Microsoft_India",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Danger_(company)",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "MileIQ",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Skype_Technologies",
            "parent": "Microsoft",
            "children": [
                {
                    "name": 'GroupMe',
                    "parent": "Skype_Technologies",
                    "children": []
                }
            ]
        },
        {
            "name": "Microsoft_Egypt",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Microsoft_Development_Center_Norway",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Nuance_Communications",
            "parent": "Microsoft",
            "children": [
                {
                    "name": "Vlingo",
                    "parent": "Nuance_Communications",
                    "children": []
                }
            ]
        },
        {
            "name": "Microsoft_Japan",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Sysinternals",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "GreenButton",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Maluuba",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "BlueTalon",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Secure_Islands",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Revolution_Analytics",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Perceptive_Pixel",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Metaswitch",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Microsoft_Store_(retail)",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Microsoft_Mobile",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Powerset_(company)",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "RiskIQ",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Xbox_Game_Studios__Xbox_Game_Studios__1",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Adallom",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "Microsoft_Press",
            "parent": "Microsoft",
            "children": []
        },
        {
            "name": "VoloMetrix",
            "parent": "Microsoft",
            "children": []
        }
    ]
})

# @app.route('/')
# @cross_origin()
# def serve():
#     return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()