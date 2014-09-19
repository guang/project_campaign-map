"""     @author:        Guang Yang
        @mktime:        9/17/2014
        @description:   tests for preprocessing
"""
import pandas as pd # NOQA
from pandas import Series, DataFrame # NOQA
from preprocess import * # NOQA
from pandas.util.testing import assert_frame_equal


def test_all_action():
    test_df = DataFrame([['type 1', 'type 0', 'type 2'],
                         ['type 0', 'type 1', 'type 1']],
                        columns=['1/1', '1/2', '1/3'])
    test_cols = ['1/1', '1/2', '1/3']
    test_action_list = all_action(test_df, test_cols)
    assert test_action_list.tolist() == ['type 0', 'type 1', 'type 2']


def test_rot2spin():
    test_df = DataFrame([[13, 12, 'Light', 3],
                         ['Medium', 'Light', 4, 5]])
    test_df_ans = DataFrame([[13, 12, 2, 3],
                             [4, 2, 4, 5]])
    # assert rot2spin(test_df) == test_df_ans
    assert_frame_equal(rot2spin(test_df), test_df_ans)
