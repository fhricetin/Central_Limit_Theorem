import numpy as np
import random
from matplotlib import pyplot as plt

def getValues(i):
    sum = 0
    for j in range(i):
        value = random.uniform(0,1)
        sum += value
    return sum

def printMeanAndStd(mean,std,given_input):
    print("The mean of experiment {} is : {}".format(given_input,mean))
    print("The standart deviation of experiment {} is : {}".format(given_input,std))

def showPlots(p1,p2,p3):
    plt.hist(p1, 100, density=True, facecolor='m')
    plt.plot(p2, p3, linewidth=2, color="b")
    plt.show()


asked_input = int(input("Which experiment do you want to calculate?"))

array = []

if(asked_input == 1):
    for i in range(200000):
        array.append(getValues(2))
    M = sum(array) / len(array)
    S = np.std(array)
    printMeanAndStd(M,S,asked_input)
    x = M + S * np.random.randn(200000)
    x2 = np.random.normal(M,S,200000)
    x1 = np.linspace(0, 2, 100)
    f = 1 / (S * np.sqrt(2 * np.pi)) * np.exp(- (x1 - M) ** 2 / (2 * S ** 2))

    showPlots(x, x1, f)



elif(asked_input == 2):
    for i in range(200000):
        array.append(getValues(4))
    M = sum(array) / len(array)  #mean
    S = np.std(array)   #standart deviation
    printMeanAndStd(M, S, asked_input)
    x = M + S * np.random.randn(200000)
    x1 = np.linspace(0, 4, 100)
    f = 1 / (S * np.sqrt(2 * np.pi)) * np.exp(- (x1 - M) ** 2 / (2 * S ** 2))

    showPlots(x, x1, f)


elif(asked_input == 3):
    for i in range(2000):
        array.append(getValues(50))
    M = sum(array) / len(array)  # mean
    S = np.std(array)  # standart deviation
    printMeanAndStd(M, S, asked_input)
    x = M + S * np.random.randn(200000)
    x1 = np.linspace(0, 50, 100)
    f = 1 / (S * np.sqrt(2 * np.pi)) * np.exp(- (x1 - M) ** 2 / (2 * S ** 2))

    showPlots(x, x1, f)

elif(asked_input == 4):
    for i in range(2000):
        value1 = random.uniform(0, 200)
        array2 = []
        array2.append(value1)
        for i in range(49):
            if(value1 < 99):
                value1 = random.uniform(0, 200)
            else:
                value1 = random.uniform(98, 102)
            array2.append(value1)
        array.append(sum(array2))
    M = sum(array) / len(array)  # mean
    S = np.std(array)  # standart deviation
    printMeanAndStd(M, S, asked_input)
    x = M + S * np.random.randn(200000)
    x1 = np.linspace(0, 10000, 100)
    f = 1 / (S * np.sqrt(2 * np.pi)) * np.exp(- (x1 - M) ** 2 / (2 * S ** 2))

    showPlots(x, x1, f)

elif(asked_input == 5):
    for i in range(1000):
        array3 = []
        for j in range(50):
            param1 = random.uniform(0,1)
            param2 = random.uniform(0,1)
            if(param2 > param1):
                array3.append(random.uniform(param1, param2-param1))
            else:
                array3.append(random.uniform(param2, param1-param2))
        array.append(sum(array3))
    M = sum(array) / len(array)  # mean
    S = np.std(array)  # standart deviation
    printMeanAndStd(M, S, asked_input)
    x = M + S * np.random.randn(200000)
    x1 = np.linspace(0, 50, 100)
    f = 1 / (S * np.sqrt(2 * np.pi)) * np.exp(- (x1 - M) ** 2 / (2 * S ** 2))

    showPlots(x, x1, f)







