
import os
import configparser
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import re
import io
import client.database.db as db
sys.path.append('../')

def import_pub_data():
    parser = configparser.ConfigParser()
    parser.read('client\\settings.ini')

    first_c_lower = parser.get('PUBLICATION_DATA', 'FIRST_C_LOWER')
    second_c_lower = parser.get('PUBLICATION_DATA', 'SECOND_C_LOWER')
    third_c_lower = parser.get('PUBLICATION_DATA', 'THIRD_C_LOWER')
    db_path = parser.get('SYSTEM_SETTINGS', 'THIRD_C_LOWER')

    return first_c_lower, second_c_lower, third_c_lower

class StatisticsExportation:

    def __init__(self, from_year, to_year, agg_data=False, stat_diagrams=False, department_stats=False, outpath='C:\\', outfile_name='', df=None):
        self.first_cat, self.second_cat, self.third_cat = import_pub_data()
        self.outpath = outpath
        self.worksheet = None
        if not outfile_name:
            self.outfile_name = f'STAT_EXPORT_{from_year}-{to_year}' if from_year != to_year else f'STAT_EXPORT_{from_year}'

        if not df:
            records = db.get_records_by_year([from_year, to_year])
            self.df = pd.DataFrame(records)
            self.df.columns = records.keys()

    def create_num_of_documents_by_year_plot(self):
        '''
        Creates a plot which shows the process
        of the number of documents over the years
        '''

        num_of_docs_by_year = self.df.groupby(['Year']).size()   # get number of documents by year

        years = self.df['Year'].unique() # get unique values of years from data frame

        plt.xlabel('Year')
        plt.ylabel('Number of Docs')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, num_of_docs_by_year)    # create the plot

        plt.show()  # Generate the plot

        return plot

    def create_num_of_documents_by_year_plot_top_ten(self):
        '''
        Creates a plot which shows the evolution
        of the number of documents, whose average percentile is over 90, over the years
        '''

        top_ten_rows = self.df.loc[self.df['Average Percentile'] >= 90.0]

        num_of_docs_per_year_top_ten = top_ten_rows.groupby(['Year']).size()   # get number of documents in top ten percentile by year

        years = self.df['Year'].unique() # get unique values of years from data frame

        plt.xlabel('Year')
        plt.ylabel('Number of Docs (Top 10)')

        plt.gca().yaxis.set_major_locator(mticker.MultipleLocator(1)) 

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, num_of_docs_per_year_top_ten)    # create the plot

        plt.show()  # Generate the plot

        return plot

    def create_citescore_mean_by_year_plot(self):
        '''
        Creates a plot which shows the evolution
        of citescore mean over the years
        '''

        citescores = self.df.groupby('Year')['CiteScore'].mean()

        years = self.df['Year'].unique()

        plt.xlabel('Year')
        plt.ylabel('CiteScore (Mean)')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, citescores)    # create the plot

        plt.show()  # Generate the plot

        return plot

    def create_avg_percentile_by_year_plot(self):
        '''
        Creates a plot which shows the evolution
        of average percentile mean over the years
        '''

        citescores = self.df.groupby('Year')['Average Percentile'].mean()    # find mean by year

        years = self.df['Year'].unique()

        plt.xlabel('Year')
        plt.ylabel('Average Percentile (Mean)')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.plot(years, citescores)    # create the plot

        plt.show()  # Generate the plot

        return plot

    def create_citescore_max_by_year_barplot(self):
        '''
        Creates a plot which shows the evolution
        of maximum CiteScore over the years
        '''

        years = self.df['Year'].unique()
        citescore_max = self.df.groupby('Year')['CiteScore'].max()

        plt.xlabel('Year')
        plt.ylabel('Maximum CiteScore')

        plt.gca().xaxis.set_major_locator(mticker.MultipleLocator(1))   # only integers in year axis

        plot = plt.bar(years, citescore_max)   # create the barplot

        plt.show()

        return plot

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
            max_year = self.df['Year'].max().astype(int)
            min_year = self.df['Year'].min().astype(int)
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

        first_category = df.loc[df['Average Percentile'] >= self.first_cat]['Average Percentile']    # find all the journals with average percentile >= 95%

        second_category = df.loc[(df['Average Percentile'] >= self.second_cat) & (df['Average Percentile'] <= 94.99)]['Average Percentile']

        third_category = df.loc[(df['Average Percentile'] >= self.third_cat) & (df['Average Percentile'] <= 79.99)]['Average Percentile']

        fourth_category = df.loc[(df['Average Percentile'] <= self.third_cat)]['Average Percentile']

        values = [fourth_category.size, third_category.size, second_category.size, first_category.size]

        plt.xlabel('Average Percentile')
        plt.ylabel('Number of Docs')

        barplot = plt.bar(categories, values)    # create the barplot

        imgdata = io.BytesIO()
        plt.savefig(imgdata)

        return imgdata

    def create_authors_overall_ranking_excel(self):
        '''
        Creates a plot which shows the evolution
        of maximum CiteScore over the years
        '''

        professors = db.fetch_professors_from_db()

        author_lst = self.create_author_list()

        pd.DataFrame(self.create_final_list(professors)).to_excel(self.outpath+self.outfile_name)

    def write_to_excel(self):
        '''
        Takes a list of dictionaries (sources)
        and writes all the info to excel file
        '''
        import xlsxwriter

        workbook = xlsxwriter.Workbook(self.outpath)
        worksheet = workbook.add_worksheet('Table')

        bold = workbook.add_format({'bold': True})

        for header in list(results_lst[0]):
            col=list(results_lst[0]).index(header) # we are keeping order.
            worksheet.write(0, col, header, bold) # we have written first row which is the header of worksheet also.

        green_format = workbook.add_format({'bg_color': '#009933'})
        blue_format = workbook.add_format({'bg_color': '#0099ff'})
        yellow_format = workbook.add_format({'bg_color': '#ffcc00'})
        red_format = workbook.add_format({'bg_color': '#ff3333'})

        row=1
        for d in results_lst:
            for _key,_value in d.items():
                col=list(results_lst[0]).index(_key)
                if d['Average Percentile'] >= 95.0:
                    worksheet.set_row(row, cell_format=green_format)
                elif d['Average Percentile'] >= 80.0:
                    worksheet.set_row(row, cell_format=blue_format)
                elif d['Average Percentile'] >= 50.0:
                    worksheet.set_row(row, cell_format=yellow_format)
                else:
                    worksheet.set_row(row, cell_format=red_format)
                worksheet.write(row,col,_value)
            row+=1 #enter the next row

        worksheet = workbook.add_worksheet('Barlplot')

        imgdata = create_percentile_rank_barplot(pd.DataFrame(results_lst))
        
        worksheet.insert_image(0,0, '', {'image_data': imgdata})
        workbook.close()
