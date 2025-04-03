import pandas as pd
import csv
from datetime import datetime, timedelta
import os
import sys
import glob
import warnings

warnings.filterwarnings('ignore')

DEFAULT_FILE = "PIRA-UVA-UVB.dat"

def setup():
    """ Initialize the script checking for basic "export" folder and selecting proper
        location of AWS

        Returns
        -------
        location : string
            string that represents the location of station
    """
    if not os.path.exists('export'):
        os.makedirs('export')
    
    if not os.path.exists('export/RAD'):
        os.makedirs('export/RAD')

    f = open(os.getcwd() + '/locations', "r")
    lines = f.readlines()
    for (i, item) in enumerate(lines, 1):
        print(i, item)
    try:
        location = lines[int(input("Index of location: "))-1]
    except IndexError:
        print("Index out of range, defaulting to NN-NN-AR")
        location = "NN-NN-AR"

    print("Location selected: " + location)

    return  location.strip('\n')

def split(location, file):
    """ Reads *.dat file. Output from Campbell datalogger
        
        Input: station loc, file names
        Output: file splited by dates.
    """
    
    # save original header
    with open(file) as input_file:
        head = [next(input_file) for _ in range(4)]
    
    # read file
    hd = pd.read_csv(file)
    df = pd.read_csv(file, skiprows=[1, 3, 4])

    # set header for df
    df.columns = df.iloc[0]
    df = df[1:]
    
    # drop empty columns
    n=2
    df = df.iloc[:,:-2]

    # split df into csv, add original header
    df['TS'] = pd.to_datetime(df['TS'], format='mixed')

    for i in set(df['TS'].dt.date):
        # check for folders
        if type(i) is pd._libs.tslibs.nattype.NaTType:
            print("NAT")
        else:
            if not os.path.exists('export/RAD/' + i.strftime('%Y')):  
                os.mkdir('export/RAD/' + i.strftime('%Y'))  
            if not os.path.exists('export/RAD/' + i.strftime('%Y/%m')):  
                os.mkdir('export/RAD/' + i.strftime('%Y/%m'))  
        
            f = open(f"export/RAD/{i.strftime('%Y/%m/'+ location +'-%Y-%m-%d')}.csv", "w")
            f.writelines(head)
            f.close()
            data = df[(df['TS'].dt.date >= i) & (df['TS'].dt.date < i+timedelta(days=1))]
        

        
            data.to_csv(f"export/RAD/{i.strftime('/%Y/%m/'+ location +'-%Y-%m-%d')}.csv", index=False, mode= 'a', header=False)

location = setup()

try:
    droppedFile = sys.argv[1] 
    file_list = sys.argv.pop(0)
    for arg in sys.argv:
        print("Processing: " + arg)
        split(location, arg)

except IndexError:
    print("No file dropped, searching on root folder")
    samples = glob.glob('./RAD/Series/*.dat') + glob.glob('./RAD/Series/*.backup')
    for name in samples:
        print("Processing: " + name)
        split(location, name)
    
quit()
