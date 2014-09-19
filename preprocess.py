"""     @author:        Guang Yang
        @mktime:        2014/07/17
        @description:   Preprocess raw .csv data into workable form in DataFrame
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame # NOQA


csv_file = 'data/20140815.csv'

spins_df = pd.read_csv(csv_file)


def all_action(df, cols):
    """ finds all possible action taken by the stations
    -- Args --
    df:     the dataframe to look
    cols:   column names under which to search
    -- Returns --
    action_list:    an ndarray of all possible actions """

    action_list = []
    for i in cols:
        action_list = np.union1d(df[i].unique().tolist(), action_list)
    return action_list


def rot2spin(rot_df):
    """ converts rotations (light, medium) to number of spins per week
    Light -> 2 spins
    Medium -> 4 spins
    -- Args --
    rot_df:     the dataframe with rotations in light/medium
    -- Returns --
    spin_df:    converted dataframe with spin numbers instead of rotations """

    spin_df_med = rot_df.replace('Light', 2)
    spin_df = spin_df_med.replace('Medium', 4)
    return spin_df


def rm_strings(df):
    pass


if __name__ == '__main__':
    # clean rotation numbers
    spins_df = rot2spin(spins_df)
    possible_action = all_action(spins_df,
                                 ['6/9', '6/16', '6/23', '6/30', '7/7',
                                  '7/14', '7/21', '7/28', '8/4', '8/11'])
