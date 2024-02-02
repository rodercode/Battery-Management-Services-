# Import
from crud_operations import fetched_data
from crud_operations import create

# Get charging status of the EVs battery   
def get_charge(): 
    urlPath = "charge"
    data = fetched_data(urlPath)

    # Display data
    print(f"Charging status: {data}%")


# Change the charging status of the EVs battery
def charge_battery(state):
    urlPath = "charge"
    create(urlPath, {'charging': state})
    
    print(f"Charging status: {state}")

# Discharge the EVs battery
# Reset the battery to 20%
def discharge_battery(state):
    urlPath = "discharge"
    create(urlPath, {'discharging': state})
    
    print(f"Discharging status: {state}")

# # Stop the chargin session
# # Enter json body: {'charging': 'off'}
# def stop_charge():
#     headers = {'Content-Type': 'application/json'}
    
#     # JSON request payload
#     payload = {'charging': 'off'}
    
#     # Send POST request to the server
#     response = requests.post(url + "charge", data=json.dumps(payload), headers=headers)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse JSON response and deliver dict or list to result
#         data = response.json()
#         print(data)


# def discharge():
#     headers = {'Content-Type': 'application/json'}
    
#     # JSON request payload
#     payload = {'discharging': 'on'}
    
#     # Send POST request to the server
#     response = requests.post(url + "discharge", data=json.dumps(payload), headers=headers)
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Parse JSON response and deliver dict or list to result
#         data = response.json()
#         print(data)