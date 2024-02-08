# Import the necessary libraries
from tabulate import tabulate

# Import custom functions
from info import get_price_per_hour
from info import get_baseload

def display_table(data, headers):
    # Generate a table of the data
    table = tabulate(data, headers, tablefmt="pretty")
    print(table)

# Generate a table of price and house energy consumption for each hour
def generate_price_consumption_table():
    # Get the price per hour and household consumption
    prices = get_price_per_hour()
    consumption = get_baseload()

    # Create a list of hours
    hours = []
    for i in range(0, 24):
        hours.append(i)

    # Create a dictionary with the data
    data = {'hour': hours, 'price_per_hour': prices, 'consumption': consumption}

    # Create a table headers
    headers = ['Hour', 'Price', 'Consumption']

    # Display the table
    display_table(data, headers)

    

# Generate a table of the simulation data
def generate_simulation_table(data):
    # Create a table headers
    headers = {
        "sim_time_hour": "Hour",
        "sim_time_min": "Min",
        "base_current_load": "Total Energy",
        "battery_capacity_kWh": "Battery Capacity (kWh)",
        "price_per_hour": "Price per hour (kWh)",
        "charge": "Car Battery (%)"
    }

    # Display the table
    display_table(data, headers)     