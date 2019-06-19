import requests 
from bs4 import BeautifulSoup

URL = "https://www.cnblogs.com/grandyang/p/4606334.html"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find("table")
aList=table.findAll("a")
for i in range(len(aList)):
  print(str(aList[i])+' '+str(i))
