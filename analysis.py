import sys
import requests
import json
import meaningAnalysis
import indicoiAnalysis

x = meaningAnalysis.getAnalysis('./DataSets/ex.csv')
y = indicoiAnalysis.analyse(x['list'])

print(json.dumps(y['list']))