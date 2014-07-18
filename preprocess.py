"""     @author:        Guang Yang
        @mktime:        2014/07/17
        @description:   Preprocess raw .csv data into workable form in DataFrame
"""
import pandas as pd
from pandas import Series, DataFrame


csv_file = 'data/20140711.csv'
#def extract(csv_file):
""" Extracts the .csv file into a pandas DataFrame starting on line 7"""

week_data = pd.read_csv(csv_file, skiprows=7)
assert week_data.columns[0] == 'station' # make sure skipped correct # of rows
