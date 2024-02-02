# Client side
import requests
import json

def get_data():
    url = "http://127.0.0.1:5000"
    headers = {'Content-Type': 'application/json'}
    
    # Send GET request to the server
    get_response = requests.get(url)
    
    # Check if the GET request was successful (status code 200)
    if get_response.status_code == 200:
        # Parse JSON response for GET
        data = get_response.json()
        print(data["name"])
    
    else:
        print(f"Error after GET: {get_response.status_code}")