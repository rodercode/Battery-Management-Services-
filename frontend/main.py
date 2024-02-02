from info import get_info
from info import get_price_per_hour
from info import get_baseload
from charge import get_charge
from charge import charge_battery
from charge import discharge_battery

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

# Start charging of the EVs battery
print("\nStart charging the EVs battery")
charge_battery("on")

# Stop chargin of the EVs battery
print("\nStop charging the Evs battery")
charge_battery("off")

# Discharge the EVs battery
print("\nDischarge the EVs battery")
discharge_battery("on")









# # Start charging of the EVs battery
# print("\nStart charging the EVs battery")
# create("charge", {'charging': 'on'})


# # Stop chargin of the EVs battery
# print("\nStart charging the Evs battery")
# create("charge", {'chargin': 'off'})
