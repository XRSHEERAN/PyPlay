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

#plt.scatter(x,lst)
#plt.show()

with open('num.txt',"wb") as f:
    pickle.dump(c,f)
with open('num.txt',"rb") as f:
    t=pickle.load(f)
print(t.most_common(20))
