
import xlsxwriter
import matplotlib.pyplot as plt
import io
import pandas as pd

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

def write_to_excel(lst):
    '''
    Takes a list of dictionaries (sources)
    and writes all the info to excel file
    '''
    results_lst = lst[0]
    path = lst[1]

    workbook = xlsxwriter.Workbook(path)
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