import sqlite3
import pathlib
import pandas as pd
import os

PATH = 'C:\\Users\\Dimitris\\Desktop\\' # Set your path to the folder containing the .xlsx files
DB_PATH = str(pathlib.Path(__file__).parent.absolute())+'\\test.db'

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

def read_excel():

    file_names = os.listdir(PATH)   # Fetch all files in path

    file_names = [file for file in file_names if '.xlsx' in file]    # Filter file name list for files ending with .xlsx

    excel_lst = list()    # list that will contain all excel files

    for file in file_names:

        excel = pd.read_excel(PATH + file, index_col = False)   # Read .excel file and append to list

        excel_lst.append(excel)

    df = pd.concat(excel_lst) # merge all csv read in one data frame (df that will be used for statistics)

    df = df.dropna()

    df = df.rename(columns={"# Authors": "authors_num", "Authors": "authors", "Average Percentile": "avg_percentile", "CiteScore": 
                                "citescore", "Document Name": "doc_name", "SJR": "sjr", "SNIP": "snip", "Source Name": "source_name", "Year": "year"})

    return df

def get_all_records():

    query = """SELECT doc_name, authors_num, authors, year, source_name, avg_percentile, citescore, sjr, snip FROM documents NATURAL JOIN sources ORDER BY avg_percentile DESC"""
    cursor.execute(query)
    all_recs = cursor.fetchall()

    return all_recs

# mylst = list()

# for professor in professors:
#     mylst.append({'name': professor[0], 'surename': professor[1], 'department': professor[2]})

# print(professors)

# df[['source_name', 'citescore', 'sjr', 'snip', 'avg_percentile']].to_sql('documents', conn, index = False)

# df[['doc_name', 'authors_num', 'authors', 'year', '']].to_sql('CARS', conn, index = False)

def insert_from_excel():

    for index, row in df.iterrows():
        try:
            cursor.execute('SELECT source_id FROM sources WHERE source_name = ?', (row['source_name'],))
            source = cursor.fetchone()
            if not source:
                cursor.execute('INSERT INTO sources VALUES (null,?,?,?,?,?)', row[['source_name', 'citescore', 'sjr', 'snip', 'avg_percentile']])
                tmp_lst = list(row[['doc_name', 'authors_num', 'authors', 'year']])
                tmp_lst.append(cursor.lastrowid)
                cursor.execute('INSERT INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
            else:
                tmp_lst = list(row[['doc_name', 'authors_num', 'authors', 'year']])
                tmp_lst.append(source[0])
                cursor.execute('INSERT INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
        except Exception as e:
            pass
            # print(source)
            print(e)
            # break

    conn.commit()
    cursor.close()