# Import
from crud_operations import fetched_data
from crud_operations import create

# Get charging status of the EVs battery   
def get_charge(): 
    urlPath = "charge"
    
    # return the charging status
    return fetched_data(urlPath)

# Change the charging status of the EVs battery
def charge_battery(state):
    urlPath = "charge"
    create(urlPath, {'charging': state})

# Reset the EVs battery to 20%
def discharge_battery(state):
    urlPath = "discharge"
    create(urlPath, {'discharging': state})