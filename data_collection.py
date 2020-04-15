import requests
import json
import time

#methods
def convert(num):
    s = str(num)
    if(len(s) == 1):
        s = '0' + s
    return s
def greatest(arr):
    g = 0
    for i in arr:
        try:
            if(i > g):
                g = i
        except:
            continue
    return g

#create array of dates to put in the url of the api request
dates = []
year = 2019
for month in range(1,13):
    if(month == 2):
        bound = 28
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        bound = 30
    else:
        bound = 31
    for day in range(1,bound+1):
        dates.append(str(year) + convert(month) + convert(day))

#get all the data and put it in data.json
places = ['OAK','SCK','SFO','SJC','SMF','FAT']
data = {}
data['wind'] = []
for place in places:
    data[place] = []
    print(place)
    for date in dates:
        print(date)
        r = requests.get('https://api.weather.com/v1/location/K' + place + ':9:US/observations/historical.json?apiKey=6532d6454b8aa370768e63d6ba5a832e&units=e&startDate=' + date)
        observations = json.loads(r.text)['observations']
        temps = []
        windspeeds = []
        for observ in observations:
            t = observ["temp"]
            temps.append(t)
            if(place == 'OAK'):
                w = observ["wspd"]
                windspeeds.append(w)
        data[place].append(greatest(temps))
        if(place == 'OAK'):
            data['wind'].append(greatest(windspeeds))

print('data lengths: (should be equal)')
print(len(data['OAK']))
print(len(data['SCK']))
print(len(data['SFO']))
print(len(data['FAT']))
print(len(data['SJC']))
print(len(data['SMF']))
print(len(data['wind']))

fileName = 'data/v2/' + str(year) + '.json'
with open(fileName,'w') as outfile:
    json.dump(data, outfile)
print('json written to ' + fileName)
