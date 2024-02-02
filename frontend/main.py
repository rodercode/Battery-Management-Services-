# Client side
import requests
import json

url = "http://127.0.0.1:5000/"

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

# Get household energy consumption
# Start at 00:00 -> 24:00
# 15 minutes = 1 hour
def get_baseload():
    # Send GET request to the server
    get_response = requests.get(url + "baseload")

    # Check if the GET request was successful (status code 200)
    if get_response.status_code == 200:
        # Parse JSON reponse for GET
        data = get_response.json()
        print(data)
    
    else:
        print(f"Error after GET: {get_response.status_code}")

# Information about the hourly rate at the North Pole during a day
# Start at 00:00 during the morning
def get_price_per_hour():
    # Send GET request to the server
    get_response = requests.get(url + "priceperhour")

    # Check if the GET request was successful (status code 200)
    if get_response.status_code == 200:
        # Parse JSON reponse for GET
        data = get_response.json()
        print(data)
    
    else:
        print(f"Error after GET: {get_response.status_code}")

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

