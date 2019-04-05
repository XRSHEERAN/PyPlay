import collections
import glob
import os
import matplotlib.pyplot as plt
import pickle

path='./news/'
c=collections.Counter()
for fn in glob.glob(os.path.join(path,'*.txt')):
    #got names of txt
    count=0;
    with open(fn) as f:
        for ln in f:
            for word in ln.split():
                c[word]+=1
print('Token:'+str(sum(c.values())));
print('Type:'+str(len(c)))
print('Top Twenty:')
print(c.most_common(20))
lst=[]
for word in c.most_common(len(c)):
  lst.append(word[1])
x=range(1,len(lst)+1)
print(len(x))
plt.scatter(x,lst)
plt.savefig('grf.png')

lst=[]
for word in c.most_common(len(c)):
  lst.append(word[1])
x=range(1,len(lst)+1)
lst=[math.log(n) for n in lst]
x=[math.log(n) for n in x]
plt.scatter(x,lst)
plt.savefig('log.png')//linear
