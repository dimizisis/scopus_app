import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.ticker import FuncFormatter
import numpy as np

PATH = 'C:\\Users\\Dimitris\\Desktop\\' # Set your path to the folder containing the .xlsx files

file_names = os.listdir(PATH)   # Fetch all files in path

file_names = [file for file in file_names if '.xlsx' in file]    # Filter file name list for files ending with .xlsx

excel_lst = list()    # list that will contain all excel files

for file in file_names:

    excel = pd.read_excel(PATH + file, index_col = False)   # Read .excel file and append to list

    excel_lst.append(excel)

df = pd.concat(excel_lst) # merge all csv read in one data frame (df that will be used for statistics)

df = df.dropna()

def create_num_of_documents_by_year_plot(df):
    '''
    Creates a plot which shows the process
    of the number of documents over the years
    '''

    num_of_docs_by_year = df.groupby(['Year']).size()   # get number of documents by year

    years = df['Year'].unique() # get unique values of years from data frame

    plt.xlabel('Year')
    plt.ylabel('Number of Docs')

    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

    plot = plt.plot(years, num_of_docs_by_year)    # create the plot

    plt.show()  # Generate the plot

    return plot

def create_num_of_documents_by_year_plot_top_ten(df):
    '''
    Creates a plot which shows the evolution
    of the number of documents, whose average percentile is over 90, over the years
    '''

    top_ten_rows = df.loc[df['Average Percentile'] >= 90.0]

    num_of_docs_per_year_top_ten = top_ten_rows.groupby(['Year']).size()   # get number of documents in top ten percentile by year

    years = df['Year'].unique() # get unique values of years from data frame

    plt.xlabel('Year')
    plt.ylabel('Number of Docs (Top 10)')

    plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(1)) 

    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

    plot = plt.plot(years, num_of_docs_per_year_top_ten)    # create the plot

    plt.show()  # Generate the plot

    return plot

def create_citescore_mean_by_year_plot(df):
    '''
    Creates a plot which shows the evolution
    of citescore mean over the years (CSVs)
    '''

    citescores = df.groupby('Year')['CiteScore'].mean()

    years = df['Year'].unique()

    plt.xlabel('Year')
    plt.ylabel('CiteScore (Mean)')

    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

    plot = plt.plot(years, citescores)    # create the plot

    plt.show()  # Generate the plot

    return plot

def create_avg_percentile_by_year_plot(df):
    '''
    Creates a plot which shows the evolution
    of average percentile mean over the years (CSVs)
    '''

    citescores = df.groupby('Year')['Average Percentile'].mean()    # find mean by year

    years = df['Year'].unique()

    plt.xlabel('Year')
    plt.ylabel('Average Percentile (Mean)')

    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

    plot = plt.plot(years, citescores)    # create the plot

    plt.show()  # Generate the plot

    return plot

def create_citescore_max_by_year_barplot(df):
    '''
    Creates a plot which shows the evolution
    of maximum CiteScore over the years (CSVs)
    '''

    years = df['Year'].unique()
    citescore_max = df.groupby('Year')['CiteScore'].max()

    plt.xlabel('Year')
    plt.ylabel('Maximum CiteScore')

    plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

    plot = plt.bar(years, citescore_max)   # create the barplot

    plt.show()

    return plot

def create_authors_barplot(df):
    '''
    Creates a plot which shows the evolution
    of maximum CiteScore over the years (CSVs)
    '''

    import pathlib
    import sqlite3

    PATH = ''

    conn = sqlite3.connect(PATH)

    cursor = conn.cursor()

    query = """SELECT name, surname, department FROM professors"""
    cursor.execute(query)
    lst = cursor.fetchall()

    mylst = list()

    for dtuple in lst:
        indexes = list(df['Authors'].str.find(dtuple[1]))
        indexes = [i for i in range(len(indexes)) if indexes[i] != -1]
        print(indexes)
        average = float(df['Average Percentile'].iloc[indexes].mean())
        mylst.append({'Name': dtuple[0], 'Surname': dtuple[1], 'Department': dtuple[2], 'Average': round(average, 3) if not pd.isna(average) else 0})

    print(mylst)

# create_citescore_max_by_year_barplot(df)
# create_num_of_documents_by_year_plot(df)
# create_num_of_documents_by_year_plot_top_ten(df)
# create_citescore_mean_by_year_plot(df)
# create_avg_percentile_by_year_plot(df)
create_authors_barplot(df)