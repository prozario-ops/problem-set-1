
'''
PART 1: EXTRACT WEATHER AND TRANSIT DATA

Pull in data from two dataset
1. Weather data from visualcrossing's weather API (https://www.visualcrossing.com/weather-api)
- You will need to sign up for a free account to get an API key
-- You only get 1000 rows free per day, so be careful to build your query correctly up front
-- Though not best practice, include your API key directly in your code for this assignment
- Write code below to get weather data for Chicago, IL for the date range 10/1/2024 - 10/31/2025
- The default data fields should be sufficient
2. Daily transit ridership data for the Chicago Transit Authority (CTA)
- Here is the URL: ttps://data.cityofchicago.org/api/views/6iiy-9s97/rows.csv?accessType=DOWNLOAD"

Load both as CSVs into /data
- Make sure your code is line with the standards we're using in this class 
'''

#Write your code below
import pandas as pd
import requests
import os


# Extract visual crossing weather data for Chicago, IL
def extract_weather_data(url, params):
    """
    Extract weather data from the Visual Crossing Weather API for Chicago, 
    IL for the date range 10/1/2024 - 10/31/2025.

    Args:
        url (str): The API endpoint URL.
        params (dict): A dictionary of parameters to include in the API request.

    Returns:
        pd.DataFrame: A DataFrame containing the weather data.

    Raises:
        requests.exceptions.RequestException: If the HTTP request fails.
        ValueError: If the response cannot be parsed as JSON.
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        days = data['days']
        df = pd.DataFrame(days)

        return df
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except ValueError as e:
        print(f"Error parsing weather data: {e}")
  
    





# Extract CTA transit ridership data
def extract_transit_data():
    return None