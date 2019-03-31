import collections
import glob
import os

path='./news/'
c=collections.Counter()
for fn in glob.glob(os.path.join(path,'*.txt')):
    #got names of txt
    count=0;
    with open(fn) as f:
        for ln in f:
            for word in ln.split():
                c[word]+=1
print(c.most_common(3))
