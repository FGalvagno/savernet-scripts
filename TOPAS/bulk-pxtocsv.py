from datetime import datetime
from pypxlib import Table
import csv
import glob

samples = glob.glob('./Series/*.DB')

file = open('samples' + '.csv', 'w')

writer = csv.writer(file)

#writer.writerow(['TimeStamp', 'Total Particles', 'PM10 particles', 'PM2.5 particles', 'PM1 particles'])

for name in samples:
    pxData = Table(name)
    for row in pxData:
        data= [row['TimeStamp'].strftime("%m/%d/%Y, %H:%M:%S"), row['Total Particles'], row['PM10 particles'], row['PM2.5 particles'],row['PM1 particles']]
        if(data != ['01/01/1900, 00:00:00','####0.0','####0.0','###0.00','###0.00'] and data != ['12/31/1899, 00:00:00','ug/m^3','ug/m^3','ug/m^3','ug/m^3']):
            writer.writerow(data)
    pxData.close()


file.close()

data = csv.reader(open('samples.csv','r'))
data = sorted(data, key = lambda row: datetime.strptime(row[0], "%m/%d/%Y, %H:%M:%S"))



header = ['TimeStamp', 'Total Particles', 'PM10 particles', 'PM2.5 particles', 'PM1 particles']
with open('samples_sorted.csv', 'w', newline ='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(i for i in header)
    for j in data:
        writer.writerow(j)