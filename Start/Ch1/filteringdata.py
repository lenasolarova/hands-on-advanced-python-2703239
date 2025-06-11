# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# filter(function that decides what we want, can be lambda; dataset)
# TODO: create a subset of the data for days that had snowfall
snowdays = list(filter(lambda d: d['snow'] > 0, weatherdata))
print(len(snowdays))

# TODO: pretty-print the resulting data set
pprint.pp(snowdays)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summer_month = ['7', '8']
    return d['prcp'] >= 1 and d['date'][6:7] in summer_month

summer_rain_days = list(filter(is_summer_rain_day, weatherdata))
print("Summer rain days:", len(summer_rain_days))
