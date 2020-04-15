import json
import matplotlib.pyplot as plt

with open('results.json','r') as r:
    results = json.load(r)
with open('sets_v2/testSet.json','r') as t:
    testing = json.load(t)

thetas = results['finalThetas']   
X = testing['features']
Y = testing['output']
maxTemp = 100
maxWind = 50

def hypothesis(X, thetas):
    s = 0
    for i in range(0,len(thetas)):
        s += X[i]*thetas[i]
    return s

errors = []
errorsSum = 0
for i in range(0,365):
    hyp = hypothesis(X[i],thetas)
    print(X[i],Y[i]*maxWind,hyp*maxWind)
    error = Y[i]*maxWind - hyp*maxWind
    errors.append(abs(error))
    errorsSum += abs(error)

avgError = errorsSum/len(errors)

print(avgError)
plt.plot(errors)
plt.show()
