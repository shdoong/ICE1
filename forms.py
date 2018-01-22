import requests
import json 

API_KEY = "c3ad757f36cb48a9a8be479b520d1193"

param = {'apiKey':API_KEY, 'q':'Trump','sources':'buzzfeed'}
r = requests.get('https://newsapi.org/v2/top-headlines?', params=param)
response = json.loads(r.text)
print(response)
#print('\n\n'.join([x['title'] + '\n' + x['description'] + '\n' + x['url'] for x in response['articles']]))