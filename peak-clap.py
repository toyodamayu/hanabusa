import csv
import pandas as pd
import numpy as np
import math
import tim
import matplotlib.pyplot as plt
from scipy import signal

def getNearestValue(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]

photo=[]
xrighthand=[]
yrighthand=[]
xlefthand=[]
ylefthand=[]

fig = plt.figure()
ax1=fig.subplots()
ax2=ax1.twinx()

with open('x.csv', 'r', newline='', encoding='utf-16') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        photo.append(i)
        xrighthand.append(row[5]) #右手
        xlefthand.append(row[8]) #左手
        i+=1

photo=list(map(int,photo))
xrighthand=list(map(int,xrighthand))
xlefthand=list(map(int,xlefthand))

photo_arr = np.array(photo)
xrighthand_arr = np.array(xrighthand)
xlefthand_arr = np.array(xlefthand)

r=[]
l=[]

# x軸の話
maxid = signal.argrelmax(xrighthand_arr, order=5) # 最大値
minid = signal.argrelmin(xlefthand_arr, order=5) # 最小値

ax1.plot(xrighthand_arr,photo_arr,color="blue")  
ax2.plot(xlefthand_arr,photo_arr,c="r") 

ax1.scatter(xrighthand_arr[maxid[0]], photo_arr[maxid[0]])
for i in range(len(maxid[0])):
    ax1.text(xrighthand_arr[maxid[0][i]], photo_arr[maxid[0][i]], 'PEAK!!!')
    r.append(photo_arr[maxid[0][i]])

ax2.scatter(xlefthand_arr[minid[0]], photo_arr[minid[0]])
for i in range(len(minid[0])):
    ax2.text(xlefthand_arr[minid[0][i]], photo_arr[minid[0][i]], 'PEAK!!!')
    l.append(photo_arr[minid[0][i]])

if len(maxid[0])<len(minid[0]):
    for i in range(len(maxid[0])):
        if abs(getNearestValue(l, r[i])-r[i])<3:
            print(r[i],"枚目手拍子！！！！！")
            t=float(tim.second())
            timestart=(r[i]-3)*t
            tstart='{:.3f}'.format(timestart)
            timestop=(r[i]+3)*t
            tstop='{:.3f}'.format(timestop)
            print(tstart,"～",tstop)
else:
    for i in range(len(minid[0])):
        if abs(getNearestValue(r, l[i])-l[i])<3:
            print(l[i],"枚目手拍子！！！！！")
            t=float(tim.second())
            timestart=(l[i]-3)*t
            tstart='{:.3f}'.format(timestart)
            timestop=(l[i]+3)*t
            tstop='{:.3f}'.format(timestop)
            print(tstart,"～",tstop)

fig.savefig("accord/sample1.png")
plt.show()