"""
This file will run a unit test for the clean_up function in prep.py
"""

import pandas as pd
import pandas.api.types as ptypes

from prep import clean_up

def test_clean_up():
    """
    this function is a unit test for the clean_up function in the prep.py script
    """
    sample = {
        'Air Power': None,
        'Cadence': None, 
        'Form Power': None, 
        'Ground Time': None, 
        'Leg Spring Stiffness': None, 
        'Power': None, 
        'Vertical Oscillation': None, 
        'altitude': None, 
        'cadence': 0.0, 
        'datafile': 'activities/2675855419.fit.gz', 
        'distance': 0.0, 
        'enhanced_altitude': None, 
        'enhanced_speed': 0.0, 
        'fractional_cadence': 0.0,
        'heart_rate': 68.0,
        'position_lat': None,
        'position_long': None,
        'speed': 0.0, 
        'timestamp': '2019-07-08 21:04:03', 
        'unknown_87': 0.0, 
        'unknown_88': 300.0, 
        'unknown_90': None
    }

    input_df = pd.DataFrame([sample])
    output_df = clean_up(input_df)
    assert 'altitude' not in output_df.columns
    assert 'speed' not in output_df.columns
    assert 'unknown_87' not in output_df.columns
    assert 'datafile' not in output_df.columns
    assert 'fractional_cadence' not in output_df.columns
    assert 'unknown_88'not in output_df.columns
    assert 'unknown_90' not in output_df.columns
    assert 'Cadence' not in output_df.columns
    assert ptypes.is_datetime64_any_dtype(output_df.dtypes['timestamp'])
