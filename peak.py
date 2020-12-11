import csv
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import signal

photo=[]
xrighthand=[]
yrighthand=[]
xlefthand=[]
ylefthand=[]
y=[]

with open('x.csv', 'r', newline='', encoding='utf-16') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        photo.append(i)
        y.append(row[5]) #右手
        #y.append(row[8]) #左手
        #momor.append(row[9])
        i+=1

#with open('y.csv', 'r', newline='', encoding='utf-16') as f:
    #reader = csv.reader(f)
    #i=0
    #for row in reader:
        #photo.append(i)
        #y.append(row[5]) #右手
        #y.append(row[8]) #左手
        #momor.append(row[9]) #右腰
        #momol.append(row[12]) #左腰
        #i+=1

photo=list(map(int,photo))
y=list(map(int,y))

photo_arr = np.array(photo)
y_arr = np.array(y)

#print("photo:",photo_arr)
#print("y:",y_arr)

# ピーク値のインデックスを取得
maxid = signal.argrelmax(y_arr, order=5) # 最大値

# 描画
#Fig = plt.figure(figsize=(6, 6))
#Map1 = plt.add_subplot(111)
plt.plot(photo_arr, y_arr)
plt.scatter(photo_arr[maxid[0]], y_arr[maxid[0]])
for i in range(len(maxid[0])):
    plt.text(photo_arr[maxid[0][i]], y_arr[maxid[0][i]], 'PEAK!!!')

plt.show()