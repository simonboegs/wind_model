import json
import requests
import datetime

with open('results.json','r') as json_file:
    results = json.load(json_file)
thetas = results['finalThetas']

with open('scaling.json','r') as json_file2:
    scaling = json.load(json_file2)

def hypothesis(X, thetas):
    s = 0
    for i in range(0,len(thetas)):
        s += X[i]*thetas[i]
    return s

r1 = requests.get('https://api.weather.com/v3/wx/forecast/daily/7day?apiKey=6532d6454b8aa370768e63d6ba5a832e&geocode=37.8%2C-122.27&language=en-US&units=e&format=json')
oak = json.loads(r1.text)['temperatureMax']
r2 = requests.get('https://api.weather.com/v3/wx/forecast/daily/7day?apiKey=6532d6454b8aa370768e63d6ba5a832e&geocode=37.963%2C-121.293&language=en-US&units=e&format=json')
sck = json.loads(r2.text)['temperatureMax']

print(oak)
print(sck)

predictions = []
for i in range(0,7):
    try:
        X = [1,oak[i]/scaling['maxTemp'],sck[i]/scaling['maxTemp']]
        hyp = hypothesis(X,thetas)
        prediction = hyp * scaling['maxWind']
        predictions.append(hyp*scaling['maxWind'])
    except:
        predictions.append(-1)

weekday = datetime.datetime.now().weekday()
days = ['mon','tues','wed','thurs','fri','sat','sun']
j = 0
for i in range(weekday,7+weekday):
    if i > 6:
        i -= 7
    print(days[i] + ': ' + str(predictions[j]))
    j+=1

