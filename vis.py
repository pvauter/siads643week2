"""
This file will take pre-cleaned data and format it 
to produce a line graph visualize comparison of given variables.
"""

import matplotlib.pyplot as plt

def data_prep(df, columns):
    """
    pass in a dataframe and a list of columns to return a df with additional metrics ready to plot
    """
    plot_df = df[columns]
    plot_df = plot_df.dropna().reset_index(drop=True) #removes an NA values
    plot_dict = dict.fromkeys(columns, ['mean', 'max', 'min'])
    plot_df = plot_df.groupby('workout_count').agg(plot_dict)
    return plot_df

def data_plot(df):
    """
    plot heart rate lines as min, mean, max
    """
    ymax = df[('heart_rate', 'max')]
    ymean = df[('heart_rate', 'mean')]
    ymin = df[('heart_rate', 'min')]
    x = df.index

    #setup figure and lables
    plt.figure(figsize=(10,6))
    plt.title('Heart Rate Over Time, By Workout')
    plt.xlabel('Workout Count (#)')
    plt.ylabel('Heart Rate (bpm)')

    #plot lines
    plt.plot(x, ymax, label = 'actual max hr', color='blue', alpha=0.1)
    plt.plot(x, ymean, label = 'actual mean hr')
    plt.plot(x, ymin, label = 'actual min hr', color='blue', alpha=0.1)
    plt.fill_between(x, ymax, ymin, color='blue', alpha=0.2)

    #add target zone lines and annotate
    plt.axhline(y=90, color='red', linestyle='dotted')
    plt.axhline(y=126, color='red', linestyle='dotted')
    plt.axhline(y=153, color='red', linestyle='dotted')
    plt.text(65, 90, s='Lower bound target, Mod Exercise')
    plt.text(65, 126, s='Bound between target Mod & Vigorous')
    plt.text(65, 153, s='Upper bound target, Vigorous Exercise')
    plt.legend()
    plt.show()
