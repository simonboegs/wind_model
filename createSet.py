import json

with open('scaling.json','r') as scaling_json:
    scaling = json.load(scaling_json)
training = {}
features = []
output = []

for year in range(2010,2020):
    print(str(year))
    with open('data/v2/' + str(year) + '.json','r') as json_file:
        data = json.load(json_file)
    #oak = data["OAK"]
    #sck = data["SCK"]
    #wind = data["wind"]
    for i in range(0,365):
        #row = [1,oak[i]/scaling["maxTemp"],sck[i]/scaling["maxTemp"]]
        row = [1]
        for l in data:
            if l == 'wind':
                output.append(data[l][i] / scaling['maxWind'])
                continue
            row.append(data[l][i] / scaling['maxTemp'])
        features.append(row)
        #output.append(wind[i]/scaling["maxWind"])

training['features'] = features
training['output'] = output

fileName = 'sets_v2/trainingSet.json'
with open(fileName,'w') as outfile:
    json.dump(training, outfile)
print('json written to ' + fileName)
