
import os
import configparser
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import re
import io
sys.path.append('../')
import database.db as db

def import_pub_data():
    parser = configparser.ConfigParser()
    parser.read('settings.ini')

    first_c_lower = parser.get('PUBLICATION_DATA', 'FIRST_C_LOWER')
    second_c_lower = parser.get('PUBLICATION_DATA', 'SECOND_C_LOWER')
    third_c_lower = parser.get('PUBLICATION_DATA', 'THIRD_C_LOWER')

    return first_c_lower, second_c_lower, third_c_lower

class StatisticsExportation:

    def __init__(self, from_year, to_year, agg_data=False, stat_diagrams=False, department_stats=False, outpath='C:/export.xlsx', df=None):
        self.first_cat, self.second_cat, self.third_cat = import_pub_data()
        self.from_year = from_year
        self.to_year = to_year
        self.worksheet = None
        self.outpath = outpath
        self.export = {'agg_data': agg_data, 'stat_diagrams': stat_diagrams, 'department_stats': department_stats}
        self.df = df

        if self.df is None:
            self.df = db.get_df_by_year([from_year, to_year])

        print(self.df)

    def create_num_of_documents_per_year_plot(self):
        '''
        Creates a plot which shows the process
        of the number of documents over the years
        '''

        num_of_docs_by_year = self.df.groupby(['Year']).size()   # get number of documents by year

        years = self.df['Year'].unique() # get unique values of years from data frame

        plt.clf()

        plt.xlabel('Year')
        plt.ylabel('Number of Docs')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, num_of_docs_by_year)    # create the plot

        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_num_of_documents_per_year_plot_top_ten(self):
        '''
        Creates a plot which shows the evolution
        of the number of documents, whose average percentile is over 90, over the years
        '''

        top_ten_rows = self.df.loc[self.df['Average Percentile'] >= 90.0]

        num_of_docs_per_year_top_ten = top_ten_rows.groupby(['Year']).size()   # get number of documents in top ten percentile by year

        years = self.df['Year'].unique() # get unique values of years from data frame

        plt.clf()

        plt.xlabel('Year')
        plt.ylabel('Number of Docs (Top 10)')

        plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(1)) 

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, num_of_docs_per_year_top_ten)    # create the plot

        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_citescore_mean_per_year_plot(self):
        '''
        Creates a plot which shows the evolution
        of citescore mean over the years
        '''

        citescores = self.df.groupby('Year')['CiteScore'].mean()

        years = self.df['Year'].unique()

        plt.clf()

        plt.xlabel('Year')
        plt.ylabel('CiteScore (Mean)')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, citescores)    # create the plot

        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_avg_percentile_per_year_plot(self):
        '''
        Creates a plot which shows the evolution
        of average percentile mean over the years
        '''

        citescores = self.df.groupby('Year')['Average Percentile'].mean()    # find mean by year

        years = self.df['Year'].unique()

        plt.clf()

        plt.xlabel('Year')
        plt.ylabel('Average Percentile (Mean)')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, citescores)    # create the plot

        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_citescore_max_per_year_barplot(self):
        '''
        Creates a plot which shows the evolution
        of maximum CiteScore over the years
        '''

        years = self.df['Year'].unique()
        citescore_max = self.df.groupby('Year')['CiteScore'].max()

        plt.clf()

        plt.xlabel('Year')
        plt.ylabel('Maximum CiteScore')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.bar(years, citescore_max)   # create the barplot

        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_author_list(self):
        n=2
        author_lst = list()
        for authors in self.df['Authors']:
            author_lst.append(list(map(str.strip, re.findall(",".join(["[^,]+"] * n), str(authors)))))
        return author_lst
        
    def create_final_list(self, professors):
        final_lst = list()
        for professor in professors:
            prof_name = str(professor[1]+', '+professor[0][:1]+'.')
            indexes = list(self.df['Authors'].str.find(prof_name))
            indexes = [i for i in range(len(indexes)) if indexes[i] != -1]
            average = float(self.df['Average Percentile'].iloc[indexes].mean())
            try:
                max_year = self.df['Year'].max().astype(int)
                min_year = self.df['Year'].min().astype(int)
            except:
                max_year = int(self.df['Year'].max())
                min_year = int(self.df['Year'].min())
            final_lst.append({'Name': professor[0] + ' ' + professor[1], 'Department': professor[2], 
                                'Ranking': round(average, 3) if not pd.isna(average) else 0, 'Years': str(min_year) + ' - ' + str(max_year) 
                                                                    if min_year != max_year else min_year})

        return final_lst

    def create_percentile_rank_barplot(self):
        '''
        Creates a bar plot, which shows how many
        journals exist in each category (Average Percentile >= 95% etc.)
        '''
        categories = ['<= 50%', '50% - 79,9%', '80% - 94,99%', '>= 95%']

        first_category = self.df.loc[self.df['Average Percentile'] >= float(self.first_cat)]['Average Percentile']    # find all the journals with average percentile >= 95%

        second_category = self.df.loc[(self.df['Average Percentile'] >= float(self.second_cat)) & (self.df['Average Percentile'] < float(self.first_cat))]['Average Percentile']

        third_category = self.df.loc[(self.df['Average Percentile'] >= float(self.third_cat)) & (self.df['Average Percentile'] < float(self.second_cat))]['Average Percentile']

        fourth_category = self.df.loc[(self.df['Average Percentile'] <= float(self.third_cat))]['Average Percentile']

        values = [fourth_category.size, third_category.size, second_category.size, first_category.size]

        plt.clf()

        plt.xlabel('Average Percentile')
        plt.ylabel('Number of Docs')

        barplot = plt.bar(categories, values)    # create the barplot
        
        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_authors_overall_ranking_excel(self):

        professors = db.fetch_professors_from_db()

        author_lst = self.create_author_list()

        return pd.DataFrame(self.create_final_list(professors))

    def write_to_excel(self):
        '''
        Writes all the info to excel file
        '''

        print(self.outpath)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(path=self.outpath, engine='xlsxwriter')
        
        if self.export['agg_data']:
            self.df.to_excel(writer, sheet_name='Aggregated Data')
        
        if self.export['stat_diagrams']:
            if self.are_multiple_years():
                workbook  = writer.book
                worksheet = workbook.add_worksheet('Documents Per Year')
                worksheet.insert_image(0,0, '', {'image_data': self.create_num_of_documents_per_year_plot()})
                worksheet = workbook.add_worksheet('Top Ten Per Year')
                worksheet.insert_image(0,0, '', {'image_data': self.create_num_of_documents_per_year_plot_top_ten()})
                worksheet = workbook.add_worksheet('CiteScore Mean Per Year')
                worksheet.insert_image(0,0, '', {'image_data': self.create_citescore_mean_per_year_plot()})
                worksheet = workbook.add_worksheet('Avg Percentile Mean Per Year')
                worksheet.insert_image(0,0, '', {'image_data': self.create_avg_percentile_per_year_plot()})
                worksheet = workbook.add_worksheet('Max CiteScore Per Year')
                worksheet.insert_image(0,0, '', {'image_data': self.create_citescore_max_per_year_barplot()})
            else:
                workbook  = writer.book
                worksheet = workbook.add_worksheet('Average Percentile Rank')
                worksheet.insert_image(0,0, '', {'image_data': self.create_percentile_rank_barplot()})
                worksheet = workbook.add_worksheet('Max CiteScore Per Year')
                worksheet.insert_image(0,0, '', {'image_data': self.create_citescore_max_per_year_barplot()})

        if self.export['department_stats']:
            dep_stats = self.create_authors_overall_ranking_excel()
            dep_stats.to_excel(writer, sheet_name='Department Statistics')

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    def are_multiple_years(self):
        return int(self.from_year) != int(self.to_year)
