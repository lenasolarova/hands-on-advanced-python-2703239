# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmest = max(weatherdata, key=lambda x: x['tmax'])
print("Warmest day:", warmest['date'], "at", warmest['tmax'], "F")

# TODO: What was the coldest day in the data set?
coldest = min(weatherdata, key=lambda x: x['tmin'])
print("Coldest day:", coldest['date'], "at", coldest['tmin'], "F")

# TODO: How many days had snowfall?
# list comprehension - get each day for every day in weather data
snowdays = [day for day in weatherdata if day['snow'] > 0]
print(len(snowdays))

