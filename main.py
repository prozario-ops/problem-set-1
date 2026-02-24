

'''
You will run this problem set from main.py so set things up accordingly
'''

import src.extract
import src.transform_load

# Call functions / instanciate objects from the two analysis .py files
def main():
        # Call functions from extract.py
        weather_df= src.extract.extract_weather_data()

        # Call functions from transform_load.py
        transit_df= src.transform_load.transform_transit_data()


if __name__ == "__main__":
    main()