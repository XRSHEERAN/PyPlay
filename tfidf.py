import collections
import os
c=collections.Counter()
path='./news/098.txt'
with open(path) as f:
    for ln in f:
        for word in ln.split():
            c[word]+=1
ctrNum=c['contract']
maxNum=c.most_common(1)
print(maxNum[0][1])
