#funcionts
#
#

import time
import json
import http.client#technically dont need this.
import urllib.request
import urllib.parse
import openpyxl
import os
import datetime

def menu():
    print('1. find city and create excel')
    print('2. algo')
    print('3. salir\n')

td = datetime.datetime.now()
date = str(td.year) + '-' + str(td.month)+'-'+str(td.day)

def inCities(city):
    #funcion que revisa si ciudad esta en lista de ciudades
    #devuelve cantidad de ciudades encontradas y la lista de matches 
    cities = open('newlist.json','r')
    cj = json.load(cities)
    matches = []
    for eachC in cj:#for each city(dict) in list of cities
        if city in eachC['name'].lower():#if city parameter == city['name']
            matches.append(eachC['name'])

    cities.close()

    return len(matches),matches

apiKey = '2d538925104ad8f9427cf46bd1b876c8'

def foldCheck(city):#manage folder creation
    #returns true if we are getting info
    #false if no
    
    try:
        if os.path.exists('results/'+city):
            #it exists, then check date folder
            
            if os.path.exists('results/'+city+'/'+date):
                print('We have this information')
                return False
            else:
                os.mkdir('results/'+city+'/'+date)
                print('Created date folder in',city)
                return True
        else:
            #it dont
            #create folder with city subfolder and date subfolder
            os.mkdir('results/'+city)
            os.mkdir('results/'+city+'/'+date)
            print('Created city and date folder in Results/'+city)
            return True
    except Exception as e:
        print('foldCheck except whoops',e)

def weather(city):
    try:
        parameters = urllib.parse.urlencode({'q':city,'APPID':apiKey})
        url = 'api.openweathermap.org/data/2.5/weather?'+parameters
        if foldCheck(city):
            time.sleep(2)#sleep 2 sec to see if this is the issue.
            file = urllib.request.URLopener()
            file.retrieve(url,city+'.json')
            #file.retrieve(url,'results/'+city+'/'+date+'/'+city+'.json')
            #downloads json, puts it in folder for city and date retrieved
            #path example:
            #/results/new york/2018-6-10/new york.json
            
        #else
            #we have the info.
            
            
    except Exception as e:
        print('weather except whoops',e)
