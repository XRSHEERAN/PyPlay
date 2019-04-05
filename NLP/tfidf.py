import collections
import os
import math
import glob


idfc=collections.Counter()
path='./news/'
total=0
###
for fn in glob.glob(os.path.join(path,'*.txt')):
    #got names of txt
    total+=1

    tracker=set()
    with open(fn) as f:
        for ln in f:
            for word in ln.split():
                if word not in tracker:
                    idfc[word]+=1
                    tracker.add(word)
print(idfc['contract'])

c=collections.Counter()
path='./news/098.txt'
with open(path) as f:
    for ln in f:
        for word in ln.split():
            c[word]+=1
maxNum=c.most_common(1)[0][1]
lst=[]
for word in c:
  
    tf=c[word]/maxNum #tf
    idf=math.log(total/idfc[word],10)
    if word=='contract':
      print(tf*idf)
    pr=[word]
    pr.append(tf*idf)
    lst.append(pr)
print(sorted(lst,key=lambda l:l[1], reverse=True)[:10])
