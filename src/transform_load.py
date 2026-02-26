'''
PART 2: Merge and transform the data
- Read in the two datasets from /data into two separate dataframes
- Profile, clean, and standardize date fields for both as needed
- Merge the two dataframe for the date range 10/1/2024 - 10/31/2025
- Conduct EDA to understand the relationship between weather and transit ridership over time
-- Create a line plot of daily transit ridership and daily average temperature over the whole time period
-- For February 2025, create a scatterplot of daily transit ridership vs. precipitation
-- Create a correlation heatmap of all numeric features in the merged dataframe
-- Load the merged dataframe as a CSV into /data
-- In a print statement, summarize any interesting trends you see in the merged dataset

'''

#Write your code below
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
def transform_transit_data(load=False):
    weather_file = os.path.join('data', 'chicago_weather_range.csv')
    transit_file = os.path.join('data', 'cta_transit_ridership.csv')

    weather=pd.read_csv(weather_file)
    transit=pd.read_csv(transit_file)

    weather['datetime'] = pd.to_datetime(weather['datetime'])
    transit['service_date'] = pd.to_datetime(transit['service_date'])
    print("Loaded weather rows:", len(weather))
    print("Loaded transit rows:", len(transit))



    if load:
        print("Returning raw datasets (load=True)")
        return weather, transit




