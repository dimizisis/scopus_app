
import sqlite3
import pathlib
import pandas as pd
import os
import sys
sys.path.append('../')

PATH = 'C:/Users/Dimitris/Desktop/' # Set your path to the folder containing the .xlsx files

def read_excel(excel_filenames):

    excel_lst = list()    # list that will contain all excel files

    try:

        for file in excel_filenames:
            excel = pd.read_excel(file, sheet_name=0, index_col = False)   # Read .excel file and append to list
            excel_lst.append(excel)

        df = pd.concat(excel_lst, sort=True, join='inner') # merge all excels in one data frame (df that will be used for statistics)
        df = df.dropna()
        df = df.rename(columns={'# Authors': 'authors_num', 'Authors': 'authors', 'Average Percentile': 'avg_percentile', 'CiteScore': 
                                    'citescore', 'Document Name': 'doc_name', 'SJR': 'sjr', 'SNIP': 'snip', 'Source Name': 'source_name', 'Year': 'year'})

        df['avg_percentile'] = df['avg_percentile'].astype(float)
        df['citescore'] = df['citescore'].astype(float)
        df['sjr'] = df['sjr'].astype(float)
        df['snip'] = df['snip'].astype(float)
    except Exception as e:
        print(e)
        return False

    return df

def import_db_name():

    import configparser

    parser = configparser.ConfigParser()
    parser.read('settings.ini')

    db_name = parser.get('SYSTEM_SETTINGS', 'DATABASE')

    return db_name if '.db' in db_name else f'{db_name}.db'

DB_PATH = f'{str(pathlib.Path(__file__).parent.absolute())}/{import_db_name()}'

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

def get_all_records():
    '''
    Gets all records from Database (if exist)
    in order to create a list of tuples, which later
    can be converted to classic dataframe
    '''
    query = """SELECT doc_name, authors_num, authors, year, source_name, avg_percentile, citescore, sjr, snip FROM documents NATURAL JOIN sources ORDER BY avg_percentile DESC"""
    cursor.execute(query)
    all_recs = cursor.fetchall()

    return all_recs

def get_df_by_year(years):
    '''
    Gets all records from the database
    whose year matches with the years/year passed as
    parameter to function
    Returns a dataframe with all the records & column names
    renamed with appropriate formation (to be exported directly to excel file)
    '''

    query = """SELECT doc_name, authors_num, authors, year, source_name, avg_percentile, citescore, sjr, snip FROM documents NATURAL JOIN sources WHERE year BETWEEN ? AND ? ORDER BY avg_percentile DESC"""
    df = pd.read_sql_query(query, conn, params=years)
    df = df.rename(columns={"authors_num": "# Authors", "authors": "Authors", "avg_percentile": "Average Percentile", "citescore": 
                                "CiteScore", "doc_name": "Document Name", "sjr": "SJR", "snip": "SNIP", "source_name": "Source Name", "year": "Year"})
    return df

def get_distinct_years(order='DESC'):
    '''
    Finds all different years that exist in database (no duplicates)
    Returns the list of tuples with the years (if there are any)
    '''
    query = f"""SELECT DISTINCT year FROM documents ORDER BY year {order}"""
    cursor.execute(query)
    years = cursor.fetchall()

    return years

def perform_deletion(year):
    '''
    Based on a specific year, performs deletion
    to all records matching this year
    Returns True if deletion is completed
    '''
    queries = [f''' DELETE FROM documents WHERE year = {year}''', f''' DELETE FROM sources WHERE source_id IN (SELECT source_id FROM documents WHERE year = {year})''']
    for query in queries:
        cursor.execute(query)
    conn.commit()

    return True

def perform_deletion_all():
    '''
    Based on a specific year, performs deletion
    to all records matching this year
    Returns True if deletion is completed
    '''
    queries = [''' DELETE FROM documents''', ''' DELETE FROM sources''']
    for query in queries:
        cursor.execute(query)
    conn.commit()

    return True

def is_db_empty():
    '''
    Checks if database is empty
    Returns True if it is
    Returns False if it is not
    '''
    query = """SELECT doc_name, authors_num, authors, year, source_name, avg_percentile, citescore, sjr, snip FROM documents NATURAL JOIN sources ORDER BY avg_percentile DESC"""
    cursor.execute(query)
    row = cursor.fetchone()
    return row is None

def save_to_db(lst):
    '''
    Gets a list of records and saves to
    database appropriately
    If save is successful, returns True,
    Else returns False
    '''
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
            else:
                tmp_lst = list(row[['Document Name', '# Authors', 'Authors', 'Year']])
                tmp_lst.append(source[0])
            cursor.execute('INSERT OR IGNORE INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
        except Exception as e:
            print(e)
            return False

    conn.commit()

    return True

def insert_from_excel(filenames):
    '''
    Gets a dataframe (created from excel file)
    and saves all the records to database appropriately
    If save is successful, returns True,
    Else returns False
    '''

    df = read_excel(filenames)

    for index, row in df.iterrows():
        try:
            cursor.execute('SELECT source_id FROM sources WHERE source_name = ?', (row['source_name'],))
            source = cursor.fetchone()
            if not source:
                cursor.execute('INSERT INTO sources VALUES (null,?,?,?,?,?)', row[['source_name', 'citescore', 'sjr', 'snip', 'avg_percentile']])
                tmp_lst = list(row[['doc_name', 'authors_num', 'authors', 'year']])
                tmp_lst.append(cursor.lastrowid)
            else:
                tmp_lst = list(row[['doc_name', 'authors_num', 'authors', 'year']])
                tmp_lst.append(source[0])
            cursor.execute('INSERT OR IGNORE INTO documents VALUES (null,?,?,?,?,?)', tmp_lst)
        except Exception as e:
            print(e)
            return False

    conn.commit()
    return True

def fetch_professors_from_db():
    '''
    Fetches professors from database
    and returns a list of tuples with all the
    necessary information of each professor
    '''
    query = """SELECT name, surname, department FROM uom_professors"""
    cursor.execute(query)
    professors = cursor.fetchall()

    return professors

# insert_from_excel(read_excel())
