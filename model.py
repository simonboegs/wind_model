import json
import numpy as np
import matplotlib.pyplot as plt

#       X0 X1 X2
# Xs =  1  45 80   Ys = 5
#       1  51 71        3
#       1  57 67        6
#

def costFunction(X, y, thetas):
    m = len(X)
    sqrError = (hypothesis(X,thetas)-y)**2
    return 1/(2*m) * sqrError
    
def hypothesis(X, thetas):
    s = 0
    for i in range(0,len(thetas)):
        s += X[i]*thetas[i]
    return s

def linearRegression(Xs, Ys, thetas):
    m = len(Xs)
    a = .3
    theta0 = []
    theta1 = []
    theta2 = []
    theta3 = []
    theta4 = []
    theta5 = []
    theta6 = []
    costs = []
    for k in range(0,50000):
        print(k)
        #gradient descent
        newThetas = thetas.copy()
        for j in range(0,len(thetas)):
            #do summation
            sumArr = []
            for i in range(1,len(Ys)):
                hyp = hypothesis(Xs[i],thetas)
                sumArr.append((hyp-Ys[i])*Xs[i][j])
            #formula, stored in temp var
            newThetas[j] = thetas[j] - ( (a/m) * getSum(sumArr) )
        #update thetas simoultaneously
        thetas = newThetas.copy()
        theta0.append(thetas[0])
        theta1.append(thetas[1])
        theta2.append(thetas[2])
        theta3.append(thetas[3])
        theta4.append(thetas[4])
        theta5.append(thetas[5])
        theta6.append(thetas[6])
        miniCosts = []
        for i in range(0,len(Ys)):
            miniCosts.append(costFunction(Xs[i],Ys[i],thetas))
        costs.append(getSum(miniCosts))
        print(thetas)
    plt.plot(theta0)
    plt.plot(theta1)
    plt.plot(theta2)
    plt.plot(theta3)
    plt.plot(theta4)
    plt.plot(theta5)
    plt.plot(theta6)
    plt.show()
    return thetas
    
def getSum(arr):
    amt = 0
    for x in arr:
        amt += x
    return amt

#Pull in data from data.json file
with open('sets_v2/trainingSet.json','r') as json_file:
    training = json.load(json_file)

results = {}
results['finalThetas'] = linearRegression(training['features'],training['output'],[0,0,0,0,0,0,0])
with open('results.json','w') as outfile:
    json.dump(results,outfile)
