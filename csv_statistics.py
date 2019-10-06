import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns

PATH = 'C:/Users/Dimitris/Desktop/' # Set your path to the folder containing the .csv files

file = 'results2018.csv'

df = pd.read_csv(PATH + file, index_col = False)   # Read .csv file and append to list

def create_percentile_rank_barplot(df):
    '''
    Creates a bar plot, which shows how many
    journals exist in each category (Average Percentile >= 95% etc.)
    '''

    categories = ['<= 95', '80 - 94,9', '50 - 79,9']

    first_category = df.loc[df['Average Percentile'] >= 95.00]['Average Percentile']    # find all the journals with average percentile >= 95%

    second_category = df.loc[(df['Average Percentile'] >= 80.00) & (df['Average Percentile'] <= 94.90)]['Average Percentile']

    third_category = df.loc[(df['Average Percentile'] >= 50.00) & (df['Average Percentile'] <= 79.90)]['Average Percentile']

    values = [first_category.size, second_category.size, third_category.size]

    barplot = plt.bar(categories, values)    # create the barplot

    plt.show()  # Generate the plot

    return barplot

create_percentile_rank_barplot(df)