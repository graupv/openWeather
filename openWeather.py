#api into excel
#
#

from openWeatherFunc import *

#openweathermap.org api key
#5 day, 3 hour forecast 
#
#https://api.openweathermap.org/data/2.5/forecast?q=guatemala&APPID=


op = ''
menu()

op = input('option: ')

while op != '3':

    while not op.isdigit():
        op = input('option: ')        
    
    if op == '1':
        print('find the city\n')
        #should take a city name, check if real city
        #if real should check if it has already been req
        #if not:
        '''
    1. check if city name in json
        1.1 check if more than 1
            1.1.1 if more than 1 display and wait for decision

        '''
        city = input('City name: ').lower()
        city = city.strip()
        mat, matlist = inCities(city)
        while mat == 0:
            print('\nNo cities by that name')
            city = input('City name: ').lower()
            city = city.strip()
            mat, matlist = inCities(city)

        
        if mat == 1:
            #do the do
            print('We found',mat,'city')
            print(matlist[0])
            city = matlist[0]
            '''    
    2. get json from api
    2. create folder with city name under cities folder
        2.1
            '''
            #func for request is a go.
            weather(city)
            
        elif mat > 1:
            while mat > 1:
                print('We found',mat,'matches.')
                print('Please pick one of the following:\n')
                
                for each in matlist:
                    print(matlist.index(each),each)
                choice = input('Enter number or exact city name:')
                #now make a func for getting the right city input

                
            
            #find the one
            
        '''
    3. create excel file with each key/value from json

        '''
        #
        print()
        menu()
        op = input('option: ')
        
    elif op == '2':
        print(2)
        print()
        menu()
        op = input('option: ')
    
else:
    print('Fin.')

url = 'https://api.openweathermap.org/data/2.5/forecast?q=guatemala&APPID='+apiKey

#api.openweathermap.org/data/2.5/weather?q=

response = urlopen(url)
parsed = json.load(response)
filename = 'forecast.json'

try:
    testfile = urllib.request.URLopener()
    testfile.retrieve(url,filename)
    
except Exception as e:
    print('whoops,',e)

'''
print('parsed is json')
print('contains:\n')
for x in parsed:
    print(x,'\n')
'''
#parsed['list'] , 40 items.
'''
parsed['list'][0]['dt_txt']
fecha en formato: 
'2018-06-08 09:00:00'
'''
