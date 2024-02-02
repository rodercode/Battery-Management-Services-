# Battery Management Service
Welcome to the Battery Management Service, a Python full-stack application that allows users to effortlessly charge their car and monitor the total energy consumption throughout the day.

![chuttersnap-xJLsHl0hIik-unsplash](https://github.com/rodercode/Battery-Management-Services-/assets/54941923/9bdcd0a7-62ea-4d83-a44b-1ba5dcd35de4)
<br>


## Features
- **Effortless Charging:** With the Battery Management Service, you can easily initiate the charging process for your electric car with just a few clicks.
- **Real-time Energy Consumption:** Keep track of your car's energy consumption in real-time, allowing you to make informed decisions about when and how to charge your vehicle.
<br>

## Endpoints
The Battery Management Service provides the following endpoints for various functionalities:
information kring
simuleringstid (ett dygn = ett antal sekunder)
total energiförbrukning
EV-batteriets laddning i kWh 

- **Get Info about: /info**
  - Simulation time (one day = a certain number of seconds)
  - Total energy consumption
  - EV battery charging in kWh

- **Get household energy consumption: /baseload**
  - start at 00:00 during the morning

- **Get Energy price per hour: /priceperhour**
  - information about the hourly rate at the North Pole during a day
  - start at 00:00 during the morning

- **Check Car Battery Percentage: /charge**
  - It will display the percentage of battery charge that has been accumulated.
  
- **Post start or stop charging session: /charge**
  - json body: "charging":"on" -> start session
  - json body: "chargin":"off" -> stop session

- **Post discard to reset car's battery: /discharge**
  - set battery to 20%
<br> 

## Technologies Used
- Python
- Flask (for the backend)
<br>

## Getting Started
1. Clone the Repository
Open your command-line interface and run the following command to clone the Battery Management Service repository from GitHub:

Clone this repository to your local machine:
   ```bash
   https://github.com/rodercode/Battery-Management-Services-.git
<br>
