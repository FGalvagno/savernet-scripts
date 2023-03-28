#!/usr/bin/env python

#Built-in modules
import os
import warnings
import datetime
from datetime import timedelta
#Third-party modules
import pandas as pd
import mysql.connector as connection

#Global vars
yesterday = datetime.date.today() - datetime.timedelta(days=1)
location = ""


#DB config
config = {
  'user': 'root',
  'password': 'secret',
  'host': '127.0.0.1',
  'database': 'mtrackreport',
  'raise_on_warnings': True
}


def setup():
    """ Initialize the script, checking for basic "export" folder and selecting proper
        location of AWS
    """
    if not os.path.exists('export'):
        os.makedirs('export')

    f = open("locations", "r")
    lines = f.readlines()
    #-----------------------------------
    # Change index by station
    #1 PIL-CBA-AR
    #2 TCM-T-AR
    #3 VM-BA-AR
    #4 AEP-BA-AR
    #5 NEU-N-AR
    #6 BRC-RN-AR
    #7 TRW-CHT-AR
    #8 CR-CHT-AR
    #9 RG-SC-AR
    #-----------------------------------
    index = 1
    try:
        location = lines[index-1]
    except IndexError:
        print("Index out of range, defaulting to NN-NN-AR")
        location = "NN-NN-AR"


    print("Location selected: " + location)
    


def checkDirectory(year):
    """ Checks for year folder in ./export.
        If said folder doesn't exists, this function will create a new one.
    
        Parameters
        ----------
        year : int
            name of the folder to store data

    """
    if not os.path.exists('./export/' + str(year)):
        os.makedirs('./export/' + str(year))

def collectPriorDay():
    """ Creates a query and collects data from yesterday

        Returns
        -------
        df : pandas dataframe
            results from query

    """
    query = "SELECT * FROM historial WHERE timestamp BETWEEN '" + str(yesterday) + " 00:00:00' AND '" + str(yesterday) +  " 23:59:59' ;"

    print(query)
    df = pd.read_sql(query, mydb) 
    return df


def toCSV(df):
    """ Exports pandas df into a .csv file (append mode). This function also checks if the df param is empty

        Parameters
        ----------
        df : pandas dataframe
            data to be exported to csv
        
    """
    year = yesterday.year
    month = yesterday.month


    if df.empty:
        print("Database has no data on " + str(yesterday) + " omiting...")
        return
    else:
        print("Saving " + "{:02d}".format(month) + "-" + str(year))
        df.to_csv("export/" + str(year) + "/" + str(year) + "{:02d}".format(month) + "-" + location + ".csv", index=False, mode='a')
    return

setup()

try: 
    mydb = connection.connect(**config) #connecting to DB
except Exception as e:
    print("Connection failed")
    print(e)


checkDirectory(yesterday.year)
df = collectPriorDay()
print(df)
toCSV(df)

mydb.close()