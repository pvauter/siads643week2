"""
This file will be used to run scripts to prepare and create a visualization for health metric data.
"""

from prep import file_import, clean_up, workout_count
from vis import data_prep, data_plot

def main():
    """
    Main function to run data import, clean, prep and visualize.
    """
    full_df = file_import('strava.csv')
    cleaned_df = clean_up(full_df)
    workout_df = workout_count(cleaned_df)
    plot_df = data_prep(workout_df, columns=['workout_count', 'heart_rate'])
    data_plot(plot_df)

if __name__ == "__main__":
    main()
