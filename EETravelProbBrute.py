#!/usr/bin/env python3
import time, math, random, itertools

"""
Extended Essay: Traveling Salesman Problem
by Armaan Kapoor
Brute Force Algorithm
"""

start_time = time.time()
xValues = [] #array to store all the x values
yValues = [] #array to store all the y values

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
        if(counter == 14): # * is replace by 2 X the amount of coordinates you wish to test
            break

def distance(x1, y1, x2, y2):
    dist = math.hypot(x2 - x1, y2 - y1)
    return dist

def getdist(route):
    tempDist = []
    for i in range(len(route) - 1):
        route[i]
        route[i + 1]
        tempDist.append(distance(xValues[route[i]], yValues[route[i]], xValues[route[i + 1]], yValues[route[i + 1]]))
    # print(sum(tempDist))
    return sum(tempDist)

def main():
    getPoints()
    ListPerm = []
    for i in range(len(xValues)):
        ListPerm.append(i)
    routesIndex = list(itertools.permutations(ListPerm))
    allDist = []
    for i in routesIndex:
        allDist.append(getdist(i))
    # print()
    print(min(allDist))

main()
print("--- %s seconds ---" % (time.time() - start_time))
