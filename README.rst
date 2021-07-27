Takes a wikipedia URL with a table in the webpage and returns a dataframe or list of dataframes if there are multiple tables in the webpage.

Installation
------------
pip install wikitable

Functions
---------
wikitable(url, to_csv=False, table_number=[None], overwrite = False, names = None)
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
from wikitable import wikitable
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate'
df = wikitable(url, to_csv=True, overwrite=True, table_number=2)

