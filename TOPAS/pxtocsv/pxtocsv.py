from pypxlib import Table
import csv
from pathlib import Path
import os

samples = os.listdir('./sample')
index = 1;

print('Files detected on sample folder:')
for name in samples:
    print(str(index) + '.', name)
    index += 1


val = int(input('Index of DB to convert: ')) - 1 

pxData = Table('./sample/' + samples[val])

file = open(samples[val] + '.csv', 'w')

writer = csv.writer(file)

print('Converting DB...')

for row in pxData:
    data= [row['TimeStamp'].strftime("%m/%d/%Y, %H:%M:%S"), row['Total Particles'], row['PM10 particles'], row['PM2.5 particles'],row['PM1 particles']]
    writer.writerow(data)

print('Output saved to: ' + samples[val] + '.csv')

file.close()
