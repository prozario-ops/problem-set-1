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
def transform_transit_data():
    """
    Transform and merge the transit ridership data with the weather data, then conduct EDA to understand the relationship between weather and transit ridership over time.
        None
    Returns:
        pd.DataFrame: A merged DataFrame containing the transit ridership and weather data.

    """
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

    print(merged.head())

    #Line plot
    plt.figure(figsize=(12,6))
    plt.plot(merged['datetime'], merged['total_rides'], label='DailyTransit Ridership')
    plt.plot(merged['datetime'], merged['temp'], label='Daily Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Daily Transit Ridership and Daily Average Temperature Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join('data', 'lineplot_transit_weather.png'))
    plt.show()

    #Scatter plot for February 2025
    feb_2025=merged[(merged['datetime'] >= '2025-02-01') & (merged['datetime'] <= '2025-02-28')]
    
    plt.figure(figsize=(8,6))
    plt.scatter(feb_2025['precip'], feb_2025['total_rides'])
    plt.xlabel('Precipitation')
    plt.ylabel('Daily Transit Ridership')
    plt.title('Daily Transit Ridership vs. Precipitation (February 2025)')
    plt.tight_layout()
    plt.savefig(os.path.join('data', 'scatter_feb2025.png'))
    plt.show()

    #Correlation heatmap for all numeric features
    plt.figure(figsize=(10,8))
    sns.heatmap(
        merged.corr(numeric_only=True),
        annot=True,
        fmt=".2f",                    
        annot_kws={"fontsize": 8},    
        cmap='coolwarm',
        linewidths=0.5
    )
    plt.title('Correlation Heatmap of Numeric Features')
    plt.tight_layout()
    plt.savefig(os.path.join('data', 'correlation_heatmap.png'))
    plt.show()

    # Save merged dataframe as CSV
    output_path= os.path.join('data', 'merged_weather_transit.csv')
    merged.to_csv(output_path, index=False)
    print(f"Merged dataframe saved to {output_path}")

    # Print summary of trends
    print("Summary of Trends:")
    if merged['temp'].corr(merged['total_rides']) > 0:
        print("There is a positive correlation between temperature and transit ridership, suggesting that higher temperatures may be associated with increased transit usage.")
    else:
        print("There is a negative correlation between temperature and transit ridership, suggesting that higher temperatures may be associated with decreased transit usage.")
    if merged['precip'].corr(merged['total_rides']) > 0:
        print("There is a positive correlation between precipitation and transit ridership, suggesting that higher precipitation may be associated with increased transit usage.")
    else:
        print("There is a negative correlation between precipitation and transit ridership, suggesting that higher precipitation may be associated with decreased transit usage.")
    print("heatmap shows that there are some other weather features that also have correlations with transit ridership, such as humidity and windspeed, which could be explored further in future analyses.")
    print("Overall, the analysis suggests that weather conditions do have an impact on transit ridership, and understanding these relationships can help transit agencies better plan for fluctuations in demand based on weather patterns.")
    return merged










