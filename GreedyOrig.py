#!/usr/bin/env python3
import time, math, random
"""
Extended Essay: Traveling Salesman Problem
by Armaan Kapoor
Greedy Algorithm
"""

start_time = time.time()
xValues = [] #array to store all the x values
yValues = [] #array to store all the y values
tempDists = []

file = open('EErandomPoints.txt','r')

def getPoints():
    string = file.readline()
    arrXY = list(map(int, string.split()))

    counter = 0
    for i in arrXY:
        if(counter % 2 == 0):
            xValues.append(i)
        else:
            yValues.append(i)
        counter += 1
        if(counter == 10): # this is to test with only 5 coordinates
            break

def distance(x1, y1, x2, y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return dist

def findDist():
    val = 0 #start at the first random city
    i = 0 #iterator
    tempDists.clear()
    while(i < len(xValues) and i < len(yValues)):
        tempDists.append(distance(xValues[val], yValues[val], xValues[i], yValues[i]))

        print("(", xValues[i], ",", yValues[i], ")", end = '')
        print(": ", tempDists[i], "  -  ")
        i = i + 1

def main():
    getPoints()
    totalDist = 0
    while(len(xValues) > 1):
        findDist()
        tempDists.pop(0) # take out the 0 in the beginning
        if(len(tempDists) == 0):
            break
        index = tempDists.index(min(tempDists))
        print()
        print("min is : ", min(tempDists))
        print()
        totalDist = totalDist + tempDists[index]
        xValues.pop(0)
        yValues.pop(0)
        nextCity = xValues.pop(index)
        xValues.insert(0, nextCity)
        nextCity = yValues.pop(index)
        yValues.insert(0, nextCity)
    print()
    print(totalDist)




main()
print("--- %s seconds ---" % (time.time() - start_time))
