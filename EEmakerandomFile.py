#!/usr/bin/env python3
import random
"""
Extended Essay: Traveling Salesman Problem
by Armaan Kapoor
Makes files with random points
"""
file = open('EErandomPoints.txt','w')

xValues = [] #array to store all the x values
yValues = [] #array to store all the y values

def addPointX():
    tempX = random.randint(-200,200) #200 is random number
    xValues.append(tempX)

def addPointY():
    tempY = random.randint(-200,200) #200 is random number
    yValues.append(tempY)

def main():
    cty = 500 # 500 cities is the max
    while(cty > 0):
        addPointX()
        addPointY()
        if(xValues[500 - cty]) in zip(xValues, xValues[:-1]):
            if(yValues[500 - cty]) in zip(yValues, yValues[:-1]):
                xValues.pop(cty - 1)
                yValues.pop(cty - 1) # remove overlapping points
                cty += 1
        cty -= 1
    index = 0
    while(len(xValues) > index):
        file.write(str(xValues[index]) + " ")
        file.write(str(yValues[index]) + " ")
        index += 1
    file.close()

main()
