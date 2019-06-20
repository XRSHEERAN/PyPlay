import requests 
from bs4 import BeautifulSoup
import re

URL = "https://www.cnblogs.com/grandyang/p/4606334.html"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find("table")
aList=table.findAll("a")
tr=requests.get(aList[0]["href"])
sp=BeautifulSoup(tr.content, 'html.parser')
#matchObj = re.match( r'.*', sp.get_text(), re.M|re.I)
lft=sp.get_text().find(sp.find("a", {"id": "cb_post_title_url"}).get_text())
rgt=sp.get_text().find(r'参考资料')
print(lft)
"""


for i in aList):
  temp=str(i)
  tr=requests.get(temp)
""" 
 
