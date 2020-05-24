import requests   #imports request library
import json       #imports json library
import time       #imports time library
import datetime   #imports datetime library

cities = ["170353", "174479", "170531", "174504", "174504", "174459", "174030", "169839", "174516", "170541"] #array of location keys of required cities from AccuWeather

for city in cities: #using for loop to loop through the cities
 url = "http://dataservice.accuweather.com/currentconditions/v1/"+city+"/historical/24?apikey=UEUHmHQn3uRrNBAqfdPRFQQ8GQ9F4ZAb" #API call URL

 r = requests.get(url) #using the get method of the request module 

 content = r.content #fething the data/content

 json_data = json.loads(content) #loading it in JSON

 prediction = {} #declaring a dictionary to store the json data

 for x in json_data: #for loop to loop through the hours in the data
  prediction =  x["LocalObservationDateTime"], x["Temperature"]["Metric"]["Value"], x["WeatherText"], x["HasPrecipitation"], x["PrecipitationType"] 
  #cleaning the data
 
  with open(r"CData.txt", "a") as cleaned: #opening the local file to store the cleaned data
   json.dump(prediction,cleaned) #dumps the JSON dictionary in the local file
   cleaned.write("\n") #prints a blank line so that next hour's data can be viewed clearly






