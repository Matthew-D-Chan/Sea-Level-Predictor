import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', ax=ax)

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(df['Year'].min(), 2051))
    y = res.slope * x + res.intercept
    plt.plot(x, y, color='red', label='Line of Best Fit 1')
    # Create second line of best fit
    df_filtered = df[df['Year'] >= 2000]
    res_2 = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
    x_2 = pd.Series(range(2000,2051))
    y_2 = res_2.slope * x_2 + res_2.intercept
    plt.plot(x_2, y_2, color='purple', label='Line of Best Fit 2')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return plt.gca()