from info import get_info
from info import get_price_per_hour
from info import get_baseload
from info import get_charge

# Get information about the simulation
print("\nSimulation info")
get_info()

# Get price information for electricity area 3 in Stockholm.
print("\nPrice information for electricity area 3 in Stockholm")
get_price_per_hour()

# Retrieve information about household energy consumption during a day.
print("\nList of electricity consumption for the household")
get_baseload()


# Get charging status of the EVs battery
print("\nDisplay the status of the EVs battery")
get_charge()





# # Start charging of the EVs battery
# print("\nStart charging the EVs battery")
# create("charge", {'charging': 'on'})


# # Stop chargin of the EVs battery
# print("\nStart charging the Evs battery")
# create("charge", {'chargin': 'off'})
