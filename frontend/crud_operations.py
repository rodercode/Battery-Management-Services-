import requests
import json
from config import url

def create(url_path, payload):
    headers = {'Content-Type': 'application/json'}
        
    # Send POST request to the server
    response = requests.post(url + url_path, data=json.dumps(payload), headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and deliver dict or list to result
        data = response.json()
        print(data)


def fetched_data(url_path):
    # Send GET request to the server
    get_response = requests.get(url + url_path)

    # Check if the GET request was successful (status code 200)
    if get_response.status_code == 200:
         # Parse JSON response for GET
        data = get_response.json()
        return data

    else:
        print(f"Error after GET: {get_response.status_code}")

