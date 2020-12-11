import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

photo=[]
x=[]
y=[]
momor=[]
momol=[]
fig = plt.figure()
ax1=fig.subplots()
ax2=ax1.twinx()
with open('x.csv', 'r', newline='', encoding='utf-16') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        #if reader.line_num==1:
           #continue
        photo.append(i)
        x.append(row[5]) #右手
        y.append(row[8]) #左手
        momor.append(row[9])
        i+=1
#with open('y.csv', 'r', newline='', encoding='utf-16') as f:
    #reader = csv.reader(f)
    #i=0
    #for row in reader:
        #if reader.line_num==1:
           #continue
        #photo.append(i)
        #y.append(row[5]) #右手
        #x.append(row[8]) #左手
        #momor.append(row[9]) #右腰
        #momol.append(row[12]) #左腰
        #i+=1
photo=list(map(int,photo))
x=list(map(int,x))
y=list(map(int,y))
momor=list(map(int,momor))
momol=list(map(int,momol))
#print(x)
#print(y) 
ax1.plot(photo,y,color="blue")
ax2.plot(photo,x,c="r")
#plt.plot(x,y1)
fig.savefig("accord/sample.png")
plt.show()

