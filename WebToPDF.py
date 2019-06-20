import requests 
from bs4 import BeautifulSoup

URL = "https://www.cnblogs.com/grandyang/p/4606334.html"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.get_text())
"""

table = soup.find("table")
aList=table.findAll("a")
for i in aList):
  temp=str(i)
  tr=requests.get(temp)
""" 
 
