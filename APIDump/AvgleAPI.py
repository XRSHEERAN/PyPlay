#Attention!! This query is just for fun using the official API from avgle.com, which contains adult content. Use the query if and only if you are over 18!!!
#I wrote this just for fun and take no responsibility for any other usage
import urllib.request
import json
#url = 'https://api.avgle.com/v1/categories'
response = json.loads(urllib.request.urlopen(url).read().decode())
if response['success']:
    for i in response['response']['categories']:
      #print(i['shortname'])
