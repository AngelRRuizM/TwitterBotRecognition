import os
import json



def getCleanDataSet(dataSet):
    if os.path.exists(dataSet) == False:
        invalidDataSet()
    
    if os.path.isfile(dataSet) == False:
        invalidDataSet()
    
    dataSetFile = open(dataSet, 'r')
    firstString = dataSetFile.readline()
    if firstString == "Id,Tweet\n" :
        return test(dataSetFile)
    
    else:
        if firstString == "Tweet,Class\n" :
            return train(dataSetFile)
        
        else:
            return invalidDataSet()
        

def test(dataSetFile):
    lines = dataSetFile.readlines()
    tList = {'list': []}
    for line in lines:
        tList['list'].append({'id': getId(line), 'tweet': getTweetTest(line), 'class': '-1', 'expectedClass': '-1'})
    return tList

def getId(line):
    id = ""
    for c in line:
        if c == ',':
            break
        else:
            id = id + c
    return id

def getTweetTest(line):
    firstComma = False
    i = 0
    length = len(line)
    for c in line:
        if firstComma:
            return line[i + 1: length - 1]
        else:
            if c == ',':
                firstComma = True
                i = i + 1


def train(dataSetFile):
    lines = dataSetFile.readlines()
    tList = {'list': []}
    i = 1
    for line in lines:
        tList['list'].append({'id': i, 'tweet': getTweetTrain(line), 'class': '-1', 'expectedClass': getClass(line)})
        i = i + 1
    return tList

def getClass(line):
    length = len(line)
    i = length - 1
    for c in line:
        if line[i] == ',':
            return line[i + 1 : length - 1]
        i = i - 1

def getTweetTrain(line):
    length = len(line)
    i = length - 1
    for c in line:
        if line[i] == ',':
            return line[:i]
        i = i - 1

def invalidDataSet():
    print("The given DataSet is invalid or inexistant")
    return None