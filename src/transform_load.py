'''
part 2: Merge and transform the data
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
    #EDA and merging
    weather_file = os.path.join('data', 'chicago_weather_range.csv')
    transit_file = os.path.join('data', 'cta_transit_ridership.csv')

    weather=pd.read_csv(weather_file)
    transit=pd.read_csv(transit_file)

    weather['datetime'] = pd.to_datetime(weather['datetime'])
    transit['service_date'] = pd.to_datetime(transit['service_date'])

    weather=weather.drop_duplicates(subset='datetime')
    transit=transit.drop_duplicates(subset='service_date')

    merged=pd.merge(weather, transit, left_on='datetime', right_on='service_date', how='inner')

    mask=(merged['datetime'] >= '2024-10-01') & (merged['datetime'] <= '2025-10-31')
    merged=merged.loc[mask]

    #Line plot
    plt.figure(figsize=(12,6))
    plt.plot(merged['datetime'], merged['total_rides'], label='DailyTransit Ridership')
    plt.plot(merged['datetime'], merged['temp'], label='Daily Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Daily Transit Ridership and Daily Average Temperature Over Time')
    plt.legend()
    plt.tight_layout()
    plt.show()

    #Scatter plot for February 2025
    feb_2025=merged[(merged['datetime'] >= '2025-02-01') & (merged['datetime'] <= '2025-02-28')]
    feb=merged.loc[mask]
    plt.figure(figsize=(8,6))
    plt.scatter(feb_2025['precip'], feb_2025['total_rides'])
    plt.xlabel('Precipitation')
    plt.ylabel('Daily Transit Ridership')
    plt.title('Daily Transit Ridership vs. Precipitation (February 2025)')
    plt.tight_layout()
    plt.show()








