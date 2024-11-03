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

    auth = HTTPBasicAuth("chimeprince92@gmail.com", "ATATT3xFfGF0WRElfIQHIwTGmqVC-WR72ZPVH3WJY__VrGM6ANq1SYopSZlxpHWd4AMJD97xsFXoEamsmDP4Hq8jGj6iT9alaUmhg4O0_mmBPuMgP_K1iWZeNDCMgtPSQ_xX20hEegYFY6-rfNdslLtQOO_Z86G_-ib4KmrcTG1B3-d7PVZYkEg=1616DFD6")

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