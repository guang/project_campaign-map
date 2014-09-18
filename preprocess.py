"""     @author:        Guang Yang
        @mktime:        2014/07/17
        @description:   Preprocess raw .csv data into workable form in DataFrame
"""
import pandas as pd
import numpy as np
# from pandas import Series, DataFrame


csv_file = 'data/20140815.csv'

spins_df = pd.read_csv(csv_file)


def all_action(df, cols):
    """ finds all possible action taken by the stations
    Args
    df:     the dataframe to look
    cols:   column names under which to search

    Returns
    action_list:    an ndarray of all possible actions """

    action_list = []
    for i in cols:
        action_list = np.union(df[i].unique(), action_list)
    return action_list
