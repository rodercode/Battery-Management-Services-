# Client side
import requests
import json

url = "http://127.0.0.1:5000/"
headers = {'Content-Type': 'application/json'}

# Simulation time (one day = a certain number of seconds)
# Total energy consumption
# EV battery charging in kWh
def get_info():
    
    # Send GET request to the server
    get_response = requests.get(url + "info")
    
    # Check if the GET request was successful (status code 200)
    if get_response.status_code == 200:
        # Parse JSON response for GET
        data = get_response.json()
        print(data)
    
    else:
        print(f"Error after GET: {get_response.status_code}")

