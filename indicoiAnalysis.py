import indicoio
import json

indicoio.config.api_key = '22a297bfe4cc78b31df93df522a1878d'

def analyse(tweets):
    
    aList = {'list': []}

    for tweet in tweets:
        aList['list'].append(getAnalysis(tweet))
    
    return aList

def getAnalysis(tweet):

    emotion = indicoio.emotion(tweet['tweet'])

    y = emotion

    z = {'expectedClass': tweet['expectedClass'], 
    'tweet': tweet['tweet'], 
    'id': tweet['id'], 
    'class': tweet['class'],
    'confidence': tweet['confidence'],
    'irony': tweet['irony'],
    'agreement': tweet['agreement'],
    'subjectivity': tweet['subjectivity'],
    'score_tag': tweet['score_tag'],
    'anger': None,
    'joy': None,
    'fear': None,
    'sadness': None,
    'surprise': None}

    if 'anger' in y:
        z['anger'] = y['anger']

    if 'joy' in y:
        z['joy'] = y['joy']

    if 'fear' in y:
        z['fear'] = y['fear']
    
    if 'sadness' in y:
        z['sadness'] = y['sadness']
    
    if 'surprise' in y:
        z['surprise'] = y['surprise']

    return z

