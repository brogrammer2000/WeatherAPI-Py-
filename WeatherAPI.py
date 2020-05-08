import requests   #imports request library
import json       #imports json library
import schedule   #imports schedule library
import time       #imports time library
import datetime   #imports datetime library

cities = ["170353", "174479", "170531", "174504", "174504", "174459", "174030", "169839", "174516", "170541"] #array of location keys of required cities from AccuWeather

def APIcall(): #putting the coode in one method so that we can pass it in scheduler

 for city in cities: #using for loop to loop through the cities
  url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+city+"?apikey=UEUHmHQn3uRrNBAqfdPRFQQ8GQ9F4ZAb&language=en-us" #API call URL

  r = requests.get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+city+"?apikey=UEUHmHQn3uRrNBAqfdPRFQQ8GQ9F4ZAb&language=en-us") #API call URL
  content = r.content #fetches the content from api in the form of string

  json_data = requests.get(url).json() #fetches the content from api in the form of JSON

  prediction = {} #declaring a dictionary to store the json data
  prediction = json_data["DailyForecasts"][0]["Day"] #extracts only the day's weather forecasts(cleans the data)
  with open("C:\Users\user\Desktop\pythonAPI\data123.txt", "a") as cleaned: #opening the local file to store the cleaned data
   json.dump(prediction,cleaned) #dumps the JSON dictionary in the local file
   cleaned.write("\n") #prints a blank line so that next day's forecast can be viewed clearly
  with open("C:\Users\user\Desktop\pythonAPI\data1234.txt", "a") as raw: #opening the local file to store the raw data
   raw.write(content) #writes the forecast content in the local file
   raw.write("\n") #prints a blank line so that next day's forecast can be viewed clearly

schedule.every().day.at("07:00").do(APIcall) #schedules the task for everyday at 7am


while True: #while loop for running the code infinetly
    schedule.run_pending() #runs the code
    time.sleep(1) #formality sleep for 1 second
