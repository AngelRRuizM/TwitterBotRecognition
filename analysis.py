import sys
import requests
import json
import meaningAnalysis
import indicoiAnalysis

x = meaningAnalysis.getAnalysis('./DataSets/train.csv', 2)
y = indicoiAnalysis.analyse(x['list'])

print(json.dumps(y['list']))