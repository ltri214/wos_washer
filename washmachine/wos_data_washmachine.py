import numpy as np
import pandas as pd
import csv
import os


filenames = os.listdir('./excel')


s_name = 'washlist.csv'
data_source = pd.read_csv(s_name)
a = list(data_source['NAME'])
b = []
for c in a:
    up = c.upper()
    b.append(up)
print(b)
saver=[]
read = pd.DataFrame()

for filename in filenames:
    print(filename)
    filename = './excel/' + filename
    mid = pd.read_excel(filename)
    read = pd.concat([read,mid],axis=0)
print(read)

read =read[['Article Title','Source Title']]
read = read.dropna()

for index, row in read.iterrows():
    print(index)
    a = row['Source Title']

    test = row['Source Title'].upper()
    if test in b:
        saver.append(row)
    else:
        print('False')

with open('result.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(saver)

file.close()
