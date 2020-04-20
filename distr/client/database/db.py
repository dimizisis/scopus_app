
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

def get_records_by_year(years):
    query = """SELECT doc_name, authors_num, authors, year, source_name, avg_percentile, citescore, sjr, snip FROM documents NATURAL JOIN sources WHERE year BETWEEN ? AND ? ORDER BY avg_percentile DESC"""
    cursor.execute(query, [years])
    all_recs = cursor.fetchall()

    return all_recs

def get_distinct_years(order='DESC'):
    query = f"""SELECT DISTINCT year FROM documents ORDER BY year {order}"""
    cursor.execute(query)
    years = cursor.fetchall()

    return years

def perform_deletion(year):

    queries = [f''' DELETE FROM documents WHERE year = {year}''', f''' DELETE FROM sources WHERE source_id IN (SELECT source_id FROM documents WHERE year = {year})''']

    for query in queries:
        cursor.execute(query)
    conn.commit()

    return True

# mylst = list()

# for professor in professors:
#     mylst.append({'name': professor[0], 'surename': professor[1], 'department': professor[2]})

# print(professors)

# df[['source_name', 'citescore', 'sjr', 'snip', 'avg_percentile']].to_sql('documents', conn, index = False)

# df[['doc_name', 'authors_num', 'authors', 'year', '']].to_sql('CARS', conn, index = False)

def save_to_db(lst):

    results_lst = lst[0]

    df = pd.DataFrame(results_lst)

    for index, row in df.iterrows():
        try:
            cursor.execute('SELECT source_id FROM sources WHERE source_name = ?', (row['Source Name'],))
            source = cursor.fetchone()
            if not source:
                cursor.execute('INSERT INTO sources VALUES (null,?,?,?,?,?)', row[['Source Name', 'CiteScore', 'SJR', 'SNIP', 'Average Percentile']])
                tmp_lst = list(row[['Document Name', '# Authors', 'Authors', 'Year']])
                tmp_lst.append(cursor.lastrowid)
                cursor.execute('INSERT OR IGNORE INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
            else:
                tmp_lst = list(row[['Document Name', '# Authors', 'Authors', 'Year']])
                tmp_lst.append(source[0])
                cursor.execute('INSERT OR IGNORE INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
        except Exception as e:
            print(e)

    conn.commit()

def insert_from_excel(df):

    for index, row in df.iterrows():
        try:
            cursor.execute('SELECT source_id FROM sources WHERE source_name = ?', (row['source_name'],))
            source = cursor.fetchone()
            if not source:
                cursor.execute('INSERT INTO sources VALUES (null,?,?,?,?,?)', row[['source_name', 'citescore', 'sjr', 'snip', 'avg_percentile']])
                tmp_lst = list(row[['doc_name', 'authors_num', 'authors', 'year']])
                tmp_lst.append(cursor.lastrowid)
                cursor.execute('INSERT OR IGNORE INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
            else:
                tmp_lst = list(row[['doc_name', 'authors_num', 'authors', 'year']])
                tmp_lst.append(source[0])
                cursor.execute('INSERT OR IGNORE INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
        except Exception as e:
            print(e)

    conn.commit()
def fetch_professors_from_db():

    query = """SELECT name, surname, department FROM uni_professors"""
    cursor.execute(query)
    professors = cursor.fetchall()

    return professors
# insert_from_excel(read_excel())
