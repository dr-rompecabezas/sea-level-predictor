import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    extension = np.arange(1880, 2051, 1)
    line_1 = [res.slope*xi + res.intercept for xi in extension]
    plt.plot(extension, line_1, 'red')

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000]
    df2x = df2['Year']
    df2y = df2['CSIRO Adjusted Sea Level']
    res2 = linregress(df2x, df2y)
    extension2 = np.arange(2000, 2051)
    line_2 = [res2.slope*i + res2.intercept for i in extension2]
    plt.plot(extension2, line_2, 'orange')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()