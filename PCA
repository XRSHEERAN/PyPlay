import numpy as np

car=np.genfromtxt('cardata.csv', dtype=None, delimiter=',', names=True)

print('Retail: '+str(np.mean(car['Retail'])))#price
print('Horse Power: '+str(np.mean(car['Horsepower'])))
print(car.dtype.names)
#Get for Eigen
cal=car[list(car.dtype.names)[2:]]
#mean

cal['Horsepower'][0]=200
std=[]
mn=[]
count=0
for word in cal.dtype.names:
  std.append(np.std(cal[word]))
  mn.append(np.mean(cal[word]))
nc=[]
for entry in cal:
  temp=[]
  for num in range(0,len(entry)):
    
    entry[num]=(entry[num]-mn[num])/std[num]
    temp.append(entry[num])
  nc.append(temp)
V=np.cov(np.array(nc).T)
ev , eig = np.linalg.eig(V)
#sort the values
print(eig)
print(ev)
idx = (ev).argsort()[::-1] 
ev = ev[idx] 
eig = eig[:,idx]
print('First: ' + str(ev[0]))
print('Corresponding Vec: '+str(eig[0]))
print('Third: ' + str(ev[2]))
print('Corresponding Vec: '+str(eig[2]))
