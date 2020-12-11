import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

w=[]
x=[]
y=[]
z=[]
people1=[]
people2=[]

with open('list.csv', 'r', newline='', encoding='utf-16') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        #if reader.line_num==1:
           #continue
        w.append(row[0])
        x.append(row[1])
        y.append(row[2])
        z.append(row[3])
        i+=1
    w=list(map(int,w))
    x=list(map(int,x))
    #y=list(map(int,y))
    z=list(map(int,z))
    people=w.count(0)
    count=int(i/people)

    for j in range(count):
        times=1
        sub=[]
        while (times!=people+1):
            sub.append(z[(j+1)*people-times])
            print(z[(j+1)*people-times])
            times+=1
        sub.sort()
        #print(j*people-1)
        #ここから人数によって変わると思う
        if people==2:
            if sub[0]==z[(j+1)*people-1]:
                people1.append([w[(j+1)*people-1],x[(j+1)*people-1],y[(j+1)*people-1],z[(j+1)*people-1]])
            else:
                people2.append([w[(j+1)*people-1],x[(j+1)*people-1],y[(j+1)*people-1],z[(j+1)*people-1]])
            if sub[0]==z[(j+1)*people-2]:
                people1.append([w[(j+1)*people-2],x[(j+1)*people-2],y[(j+1)*people-2],z[(j+1)*people-2]])
            else:
                people2.append([w[(j+1)*people-2],x[(j+1)*people-2],y[(j+1)*people-2],z[(j+1)*people-2]])
            #print(people1)
            with open("people1.csv", "a", newline="", encoding="utf-16") as f: 
                writer = csv.writer(f, dialect="excel")
                writer.writerows(people1)

            with open("people2.csv", "a", newline="", encoding="utf-16") as f: 
                writer = csv.writer(f, dialect="excel")
                writer.writerows(people2)

            people1.clear()
            people2.clear()

                
                








    








