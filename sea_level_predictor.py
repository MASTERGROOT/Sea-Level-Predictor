import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress 


def draw_scatter_plot():
    df = pd.read_csv('epa-sea-level.csv',parse_dates=['Year'])
    df['Year'] = df['Year'].dt.year
    

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    regr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(list(range(1880, 2051)))
    y = regr.slope * x + regr.intercept
    plt.plot(x, y)

    # Create second line of best fit
    df = df.loc[df['Year'] >= 2000]
    regr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(list(range(2000, 2051)))
    y = regr.slope * x + regr.intercept
    plt.plot(x, y)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea-level-predictor')
    return plt.gca()
