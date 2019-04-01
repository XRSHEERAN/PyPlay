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
    tf=word[0][1]/maxNum #tf
    idf=math.log(total/idfc[word[0][0]],10)
    lst.append(tf*idf)

