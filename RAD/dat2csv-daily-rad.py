import pandas as pd
import csv
from datetime import datetime, timedelta, date
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
    

    f = open(os.getcwd() + '/RAD/locations', "r")
    lines = f.readlines()
    location = lines[0] # select PIL location

    print("Location selected: " + location)

    return  location.strip('\n')

def split(location):
    """ Reads *.dat file. Output from Campbell datalogger
        Output: file splited by dates.
    """
    
    # save original header
    with open(os.getcwd() + "/RAD/COR_PIRA-UVA-UVB.dat") as input_file:
        head = [next(input_file) for _ in range(4)]
    print(head)
    
    # read file
    hd = pd.read_csv(os.getcwd() + "/RAD/COR_PIRA-UVA-UVB.dat")
    df = pd.read_csv(os.getcwd() + "/RAD/COR_PIRA-UVA-UVB.dat", skiprows=[1, 3, 4])

    # set header for df
    df.columns = df.iloc[0]
    df = df[1:]
    
    # drop empty columns
    n=2
    df = df.iloc[:,:-2]

    # split df into csv, add original header
    df['TS'] = pd.to_datetime(df['TS'])
    print(df.dtypes)

    yesterday = date.today()-timedelta(days=1)

    # write header
    f = open(f"export/{location+'-'+yesterday.strftime('%Y-%m-%d')}.csv", "w")
    f.writelines(head)
    f.close()
    
    # write data
    try:
        data = df[(df['TS'].dt.date >= yesterday & (df['TS'].dt.date <= date.today()))]
        data.to_csv(f"export/{location+'-'+yesterday.strftime('%Y-%m-%d')}.csv", index=False, mode= 'a', header=False)
    except Exception as e:
        print(e)
        quit()
        
location = setup()
split(location)
quit()
