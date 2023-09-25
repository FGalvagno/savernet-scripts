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
    #TODO: save header
    hd = pd.read_csv("COR_PIRA-UVA-UVB.dat")

    df = pd.read_csv("COR_PIRA-UVA-UVB.dat", skiprows=[1, 3, 4])

    df.columns = df.iloc[0]
    df = df[1:]
    #TODO: drop NaN columns

    df['TS'] = pd.to_datetime(df['TS'])



    print(df.dtypes)

    for i in set(df['TS'].dt.date):
        data = df[(df['TS'].dt.date >= i) & (df['TS'].dt.date <= i+timedelta(days=1))]
        data.to_csv(f"export/{location+'-'+i.strftime('%Y-%m-%d')}.csv",index=False)

location = setup()
split(location)
quit()