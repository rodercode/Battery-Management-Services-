import requests
import json

# Global variables
url = "http://127.0.0.1:5000/"

# Create reusuable function for POST function
def create(url_path, payload):
    headers = {'Content-Type': 'application/json'}        
    response = requests.post(url + url_path, data=json.dumps(payload), headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
       return response.json()
    
    else:
        print(f"Error after POST: {response.status_code}")

# Get reusuable function for GET function
def fetched_data(url_path):
    response = requests.get(url + url_path)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Error after GET: {response.status_code}")

