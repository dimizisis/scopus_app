
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def create_percentile_rank_barplot(df):
    '''
    Creates a bar plot, which shows how many
    journals exist in each category (Average Percentile >= 95% etc.)
    '''

    categories = ['<= 50%', '50% - 79,9%', '80% - 94,9%', '>= 95%']

    first_category = df.loc[df['Average Percentile'] >= 95.00]['Average Percentile']    # find all the journals with average percentile >= 95%

    second_category = df.loc[(df['Average Percentile'] >= 80.00) & (df['Average Percentile'] <= 94.90)]['Average Percentile']

    third_category = df.loc[(df['Average Percentile'] >= 50.00) & (df['Average Percentile'] <= 79.90)]['Average Percentile']

    fourth_category = df.loc[(df['Average Percentile'] <= 50.00)]['Average Percentile']

    values = [fourth_category.size, third_category.size, second_category.size, first_category.size]

    plt.xlabel('Average Percentile')
    plt.ylabel('Number of Docs')

    barplot = plt.bar(categories, values)    # create the barplot

    imgdata = io.BytesIO()
    plt.savefig(imgdata)

    return imgdata

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

    return plot