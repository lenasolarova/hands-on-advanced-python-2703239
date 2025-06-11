# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    if f is None:
        f = 0
    return (f - 32) * 5/9


def ToMM(i):
    if i is None:
        i = 0
    return i * 25.4


def ToKPH(s):
    if s is None:
        s = 0
    return s * 1.60934


def ToMetric(wd):
    metric_weatherdata = copy.copy(wd)
    metric_weatherdata['tmin'] = ToC(wd['tmin'])
    metric_weatherdata['tmax'] = ToC(wd['tmax'])
    metric_weatherdata['prcp'] = ToMM(wd['prcp'])
    metric_weatherdata['snow'] = ToMM(wd['snow'])
    metric_weatherdata['snwd'] = ToMM(wd['snwd'])
    metric_weatherdata['awnd'] = ToKPH(wd['awnd'])
    return metric_weatherdata

# TODO: Use map() to call ToMetric and convert weatherdata to metric
metric_weather = list(map(ToMetric, weatherdata))
print(weatherdata[0])
print(metric_weather[0])

# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0
# tuple
tuple_data = list(map(lambda d:(d['date'], Avg_Temp(d['tmax'], d['tmin'])), weatherdata))
print(tuple_data[0:5])