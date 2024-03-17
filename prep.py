"""
This file will prep workout data by importing a csv file and then cleaning it to be more usable.
"""

import pandas as pd

def file_import(data_file):
    """
    this function takes in a file path and returns a df
    """
    full_df = pd.read_csv(data_file)
    return full_df


def clean_up(df):
    """
    this function drops unneccessary columns and changes dates to the correct format
    """
    print(df.iloc[0].to_dict())
    df = df.drop(['altitude', 'speed', 'unknown_87', 'datafile', 'fractional_cadence',
                           'unknown_88', 'unknown_90', 'Cadence'], axis=1)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def workout_count(df):
    """
    this function takes in a df and formats date/time to create workout count 
    and returns an updated df with this new column
    """
    df['time_diff'] = df['timestamp'].diff()
    df.at[0, 'time_diff'] = pd.Timedelta('0 days 00:00:00')
    df['workout_count'] = 0
    i = 1

    for idx, row in df.iterrows():
        df.at[idx, 'workout_count'] = i
        if row['time_diff'].total_seconds() > 480.0:
            i += 1

    return df
