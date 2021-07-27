import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def wikitable(url, to_csv=False, table_number=[None], overwrite = False, names = None):
    '''Takes a wikipedia URL with a table in the webpage and returns a dataframe or list of dataframes if there are multiple tables in the webpage.
    This function will scrape every table in the wikipedia URL if no table_numbers are specified.

    Parameters
    ----------
    url: (Required) URL of the wikipedia webpage as a string.

    to_csv: boolean value that saves each table to a CSV if changed to True. Default is False.

    table_number: int of list of ints. The table number you want to scrape. Defaults to scrape all tables.

    overwrite: boolean value that will overwrite a CSV if there is one with the same name. Default is False.

    names: string or list of strings for what the CSV(s) will be named. Default names for the CSV(s) are table1.csv, table2.csv, etc...

    Returns
    -------
    Returns a Pandas Dataframe or a list of Pandas Dataframes if multiple tables are scraped.

    Example
    -------
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate'
    df = wikitable(url, to_csv=True, overwrite=True, table_number=2)
    '''
    
    r=requests.get(url)
    if r.status_code == 404:
        assert False, '<Response [404]>\nURL not valid.'
    soup = BeautifulSoup(r.text, 'html.parser')
    table=soup.find_all('table',{'class':"wikitable"})
    df=pd.read_html(str(table))
        
    if table_number != [None]:
        dfs = []
        try:
            if type(table_number) == int:   #if user selects one table           
                dfs.append(df[table_number - 1])
                df = dfs; del dfs
            elif type(table_number) == list:    #if user selects multiple tables by inputting a list of ints
                table_number = [int(i) for i in table_number]
                [df[i-1] for i in table_number]
                for i in table_number:
                    dfs.append(df[i-1])
                df = dfs; del dfs
        except IndexError:
            assert False, 'The table number you selected does not exist.'

    if to_csv: #if user wants to save table(s) as a csv
        if names != None: #if user wants to name the csvs
            for i, csv in enumerate(df):
                if os.path.exists(f'{names}{i+1}.csv') and overwrite == False:
                    assert False, f'{names}{i+1}.csv exists in your current working directory. If you wish to overwrite this file, change the "overwrite" parameter to True'
                csv.to_csv(f'{names}{i+1}.csv')
        else:
            for i, csv in enumerate(df):
                if os.path.exists(f'table{i+1}.csv') and overwrite == False:
                    assert False, f'table{i+1}.csv exists in your current working directory. If you wish to overwrite this file, change the "overwrite" parameter to True'
                csv.to_csv(f'table{i+1}.csv')
    if len(df) == 1:
        return df[0]
    return df