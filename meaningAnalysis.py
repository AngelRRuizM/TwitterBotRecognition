import sys
import requests
import json
import time
import readDataset

url = "https://api.meaningcloud.com/sentiment-2.1"
x = {'key': '8601f345cb8241110b493ab5e4fc7736', 
        'lang': 'auto',
        'txt': None,
        'ilang': 'en'}
headers = {'content-type': 'application/json'}
failed = 0
lastFailedId = 0

def getAnalysis(fileName):

    readDataSet = readDataset.getCleanDataSet(fileName)

    jList = readDataSet['list']
    aList = {'list': []}
    i = 0
    for tweet in jList:
        aList['list'].append(analyse(tweet, i))
        time.sleep(3)
        i = i + 1

    return(aList)

def analyse(tweet, i):

    global failed

    x['txt'] = tweet['tweet']

    response = requests.request("POST", url, data=json.dumps(x), headers=headers)

    y = json.loads(response.text)

    z = {'expectedClass': tweet['expectedClass'], 
    'tweet': tweet['tweet'], 
    'id': tweet['id'], 
    'class': tweet['class'],
    'confidence': None,
    'irony': None,
    'agreement': None,
    'subjectivity': None,
    'score_tag': None}

    if 'confidence' in y:
        z['confidence'] = y['confidence']
        failed = failed + 1
        lastFailedId = i

    if 'irony' in y:
        z['irony'] = y['irony']

    if 'agreement' in y:
        z['agreement'] = y['agreement']

    if 'subjectivity' in y:
        z['subjectivity'] = y['subjectivity']

    if 'score_tag' in y:
        z['score_tag'] = y['score_tag']

    return z

print(getAnalysis('./DataSets/ex.csv'))