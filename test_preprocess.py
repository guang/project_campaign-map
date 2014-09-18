"""     @author:        Guang Yang
        @mktime:        9/17/2014
        @description:   tests for preprocessing
"""
import pandas as pd
from pandas import Series, DataFrame
from preprocess import *


def test_all_action():
    test_df = DataFrame([['type 1', 'type 0', 'type 2'],
                         ['type 0', 'type 1', 'type 1']],
                        columns=['1/1', '1/2', '1/3'])
    test_cols = ['1/1', '1/2', '1/3']
    test_action_list = all_action(test_df, test_cols)
    assert test_action_list == ['type 0', 'type 1', 'type 2']
