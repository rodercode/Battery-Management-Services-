# Client side
import requests
import json
url = "http://127.0.0.1:5000/"

# Check car battery in percentage
# It will display the battery power in percentage
def get_charge():
    # Send GET request to the server
    get_response = requests.get(url + "charge")

    # Check if the GET request was successful (status code 200)
    if get_response.status_code == 200:
        # Parse JSON reponse for GET
        data = get_response.json()
        print(data)
    
    else:
        print(f"Error after GET: {get_response.status_code}")

# Start the chargin session
# Enter json body: {'charging': 'on'}
def start_charge():
    headers = {'Content-Type': 'application/json'}
    
    # JSON request payload
    payload = {'charging': 'on'}
    
    # Send POST request to the server
    response = requests.post(url + "charge", data=json.dumps(payload), headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and deliver dict or list to result
        data = response.json()
        print(data)

# Stop the chargin session
# Enter json body: {'charging': 'off'}
def stop_charge():
    headers = {'Content-Type': 'application/json'}
    
    # JSON request payload
    payload = {'charging': 'off'}
    
    # Send POST request to the server
    response = requests.post(url + "charge", data=json.dumps(payload), headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and deliver dict or list to result
        data = response.json()
        print(data)


def discharge():
    headers = {'Content-Type': 'application/json'}
    
    # JSON request payload
    payload = {'discharging': 'on'}
    
    # Send POST request to the server
    response = requests.post(url + "discharge", data=json.dumps(payload), headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response and deliver dict or list to result
        data = response.json()
        print(data)