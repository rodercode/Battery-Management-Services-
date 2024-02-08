# Import the necessary libraries
import time
import os

# Import custom functions
from info import get_info
from info import get_price_per_hour

from charge import get_charge
from charge import charge_battery
from charge import discharge_battery

from table_display import generate_price_consumption_table
from table_display import generate_simulation_table

# Global variables
result = [] # simulation result
starts = [] # list of start times
ends = [] # list of end times

def getUserInput(message):
    while True:
        userInput = input(message)
        if userInput.isdigit():
            break
        print("Invalid input. Please enter a number.\n")
    
    return userInput
    

def manage_charging_schedule():
    is_manage_charging_schedule_active = True
    
    while is_manage_charging_schedule_active:
        # Generate a table of the price and consumption
        generate_price_consumption_table()
       
        # Ask user to input the start and end time
        start = getUserInput("What time to start charging: ")        
        starts.append(start)

        end = getUserInput("What time to stop charging: ")
        ends.append(end)

        # Ask user if they want to add another time
        choice = input("Do you want to add another time? (y/n): ")

        # If the user does not want to add another time, break the loop
        if(choice == "n"):
            break

def start_simulation():
    is_simulation_active = True
    
    # Start the simulation
    while is_simulation_active:
        # Fetch simulation data and store it in data dictionary
        data = get_info()
        data['price_per_hour'] = get_price_per_hour()[data['sim_time_hour']]
        data['charge'] = get_charge()

        # Check if the simulation is over
        if(data['sim_time_hour'] == 0 and data['charge'] > 20):
            is_simulation_active = False

        # Start charging the battery at the specified times
        for start in starts:
            if data['sim_time_hour'] == int(start):
                charge_battery("on")
        
        # Stop charging the battery at the specified times
        for end in ends:
            if data['sim_time_hour'] == int(end):
                charge_battery("off")

        # Print simulation data
        print(f"time: {data['sim_time_hour']}:{data['sim_time_min']}")
        print(f"total energy consumption: {data['base_current_load']} Kwh")
        print(f"Battery capacity: {data['battery_capacity_kWh']} Kwh")
        print(f"Price per Kwh: {data['price_per_hour']} öre")
        print(f"Car battery: {data['charge']}%")

        # Loop every second
        time.sleep(1)

        # Clear the console
        os.system('cls')
        
        # Append the data to the result list
        result.append(data)

manage_charging_schedule()
discharge_battery("on")
start_simulation()
generate_simulation_table(result)

