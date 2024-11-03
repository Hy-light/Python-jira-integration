from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# Creating a flask app instance
'''
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World'

app.run('0.0.0.0')
'''

# Creating our jira ticket
app = Flask(__name__)

@app.route("/createJIRA", methods=['POST'])
def creatJIRA():
    url = "https://chimeprince92.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("chimeprince92@gmail.com", "api_token")

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "My first jira ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10009"
        },

        "project": {
        "key": "PJ"
        },
        "summary": "First Jira Ticket",
    },
    "update": {}
    } )

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)

# MY PUBLIC IP:2.122.230.161