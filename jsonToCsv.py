import os
import json

dataSetFile = open('./analysisTrain.json', 'r')
jsonString = dataSetFile.read()

tweets = json.loads(jsonString)

print('tweet,confidence,agreement,score_tag,subjectivity,irony,joy,anger,fear,sadness,surprise,class')

for tweet in tweets:
    y = tweet['tweet']+','+str(tweet['confidence'])+','+str(tweet['agreement'])+','+str(tweet['score_tag'])+','+str(tweet['subjectivity'])+','+str(tweet['irony'])+','+str(tweet['joy'])+','+str(tweet['anger'])+','+str(tweet['fear'])+','+str(tweet['sadness'])+','+str(tweet['surprise'])+','+tweet['class']
    print(y.encode("utf-8"))