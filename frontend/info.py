# import custom functions
from crud_operations import fetched_data

# Get information about the simulation
def get_info():
    urlPath = "info"
    return fetched_data(urlPath)

# Get price information for electricity area 3 in Stockholm
def get_price_per_hour():
    urlPath = "priceperhour"
    return fetched_data(urlPath)

# Retrieve information about household energy consumption during a day
def get_baseload():
    urlPath = "baseload"
    return fetched_data(urlPath)
