import pandas as pd
import csv
from datetime import datetime, timedelta
import os

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

def split(location):
    """ Reads *.dat file. Output from Campbell datalogger
        Output: file splited by dates.
    """
    
    # save original header
    with open("COR_PIRA-UVA-UVB.dat") as input_file:
        head = [next(input_file) for _ in range(4)]
    print(head)
    
    # read file
    hd = pd.read_csv("COR_PIRA-UVA-UVB.dat")
    df = pd.read_csv("COR_PIRA-UVA-UVB.dat", skiprows=[1, 3, 4])

    # set header for df
    df.columns = df.iloc[0]
    df = df[1:]
    
    # drop empty columns
    n=2
    df = df.iloc[:,:-2]

    # split df into csv, add original header
    df['TS'] = pd.to_datetime(df['TS'])
    print(df.dtypes)
    for i in set(df['TS'].dt.date):
        f = open(f"export/{location+'-'+i.strftime('%Y-%m-%d')}.csv", "w")
        f.writelines(head)
        f.close()
        data = df[(df['TS'].dt.date >= i) & (df['TS'].dt.date <= i+timedelta(days=1))]
        data.to_csv(f"export/{location+'-'+i.strftime('%Y-%m-%d')}.csv", index=False, mode= 'a', header=False)

location = setup()
split(location)
quit()
