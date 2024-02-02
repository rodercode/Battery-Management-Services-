# Imports
from crud_operations import fetched_data

# Get simulation information
def get_info():
    urlPath = "info"
    data = fetched_data(urlPath)
    
    # Display data 
    print(f"time: {data['sim_time_hour']}:{data['sim_time_min']}")
    print(f"total energy consumption: {data['base_current_load']}Kwh")
    print(f"Battery capacity: {data['battery_capacity_kWh']}Kwh")

# Get price information for electricity area 3 in Stockholm
def get_price_per_hour():
    urlPath = "priceperhour"
    data = fetched_data(urlPath)

    # Display data
    print("Price per hour: ", data)

# Retrieve information about household energy consumption during a day
def get_baseload():
    urlPath = "baseload"
    data = fetched_data(urlPath)

    # Display data
    print("Energy level per hour: ", data)

# Get charging status of the EVs battery   
def get_charge(): 
    urlPath = "charge"
    data = fetched_data(urlPath)

    # Display data
    print(f"Charging status: {data}%")