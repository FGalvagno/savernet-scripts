#!/usr/bin/env python

#Built-in modules
import os
import warnings
import datetime
from datetime import timedelta
#Third-party modules
import pandas as pd
import mysql.connector as connection


def setup():
    """ Initialize the script, asking for DB credentials, checking for basic "export" folder and selecting proper
        location of AWS
    """
    if not os.path.exists('export'):
        os.makedirs('export')

    f = open("locations", "r")
    lines = f.readlines()
    for (i, item) in enumerate(lines, 1):
        print(i, item)
    try:
        location = lines[int(input("Index of location: "))-1]
    except IndexError:
        print("Index out of range, defaulting to NN-NN-AR")
        location = "NN-NN-AR"

    print("Location selected: " + location)
    
    host = input("Host (localhost): " or "localhost" )
    database = input("MySQL DB name (mtrackreport): " or "mtrackreport")
    user = input("DB user: " or "root")
    passwd = input("Password (leave blank for none): ")


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

def collect(year, month):
    """ Collects data from MySQL server, within specified date

        Parameters
        ----------
        year : int
        month : int
            date of data to be retrieved

        Returns
        -------
        df : pandas dataframe
            results from query
    """
    query = "SELECT * FROM historial WHERE timestamp BETWEEN '" + str(year) + "-" + str(month) + "-01 00:00:00' AND '" + lastDate(year, month) + " 23:59:00';"
    print(query)
    df = pd.read_sql(query, mydb) 
    return df


def toCSV(year, month, df):
    """ Exports pandas df into a .csv file. This function also checks if the df param is empty

        Parameters
        ----------
        year : int
        month : int
            date of data
        df : pandas dataframe
            data to be exported to csv
        
    """
    if df.empty:
        print("Database has no data on " + str(month) + "-" + str(year) + " omiting...")
        return
    else:
        print("Saving " + "{:02d}".format(month) + "-" + str(year))
        df.to_csv("export/" + str(year) + "/" + str(year) + "{:02d}".format(month) + "-AR-CBA-PILAR.csv", index=False)
    return


yesterday = (datetime.date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
print(yesterday)