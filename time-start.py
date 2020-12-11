import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x=[]
y=[]
z=[]

with open('list.csv', 'r', newline='', encoding='utf-16') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        #if reader.line_num==1:
           #continue
        x.append(row[0])
        y.append(row[1])
        z.append(row[2])
        i+=1

y=list(map(int,y))

if y[0]==1:
    print(z[0])

csv=1
for csv in range(i):
    if y[csv]==1 and y[csv-2]==0:
        print(z[csv])



