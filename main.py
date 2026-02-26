

'''
You will run this problem set from main.py so set things up accordingly
'''

import src.extract
import src.transform_load
#& c:\INST737\problem-set-1-INST737\problem-set-1\.venv\Scripts\python.exe c:/INST737/problem-set-1-INST737/problem-set-1/main.py
# Call functions / instanciate objects from the two analysis .py files
api_key = 'W7XQAFQPEA7NJRQ5YST23WKT3'
location = 'Chicago,IL'
start_date = '2024-10-01'
end_date = '2025-10-31'


url= f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{start_date}/{end_date}'
params = {
    'unitGroup':'us',
    'include':'days',
    'key': api_key,
    'contentType':'json'
}
def main():
        # Call functions from extract.py
        #weather_df= src.extract.extract_weather_data(url, params)
        #if weather_df is not None:
                print(weather_df.head())
       # else:
         #      print('None returned')
        # Call functions from transform_load.py
        # transit_df= src.transform_load.transform_transit_data()


if __name__ == "__main__":
    main()