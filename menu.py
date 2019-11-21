
import init
import ui.login_ui as login_ui
import csv
import menu
import ui.menu_ui as menu_ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from queue import deque
from PyQt5 import QtCore
import re

browser = None

def update_browser(updated_browser):
    '''
    Updates the browser with its latest form
    '''
    global browser
    browser = updated_browser

def logout():

    '''
    This function brings user to login window
    in order to login again with the same or
    different scopus account
    Triggered on Logout click (menu bar) or on CTRL+L pressed

    '''
    try:
        sign_in_link_id = 'signin_link_move'
        sign_in_with_different_id = 'bdd-elsSecondaryBtn'

        browser.get('https://id.elsevier.com/ext/ae-logout?platSite=SC%2Fscopus&return_to=https%3A%2F%2Fwww.scopus.com%2Flogout.uri')

        sign_in = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, sign_in_link_id)))
        sign_in.click()

        sign_in_with_different = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, sign_in_with_different_id)))
        sign_in_with_different.click()

        return True
    except:
        return False

def browse_to_search_page():

    if browser.current_url != init.search_url:
            browser.get(init.search_url)
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, '_pendo-close-guide_'))).click()
    except:
        pass

def write_to_csv(list):
    '''
    Takes a list of dictionaries (sources)
    and writes all the info to csv file
    '''
    results_lst = list[0]
    csv_path = list[1]
    keys = results_lst[0].keys()
            
    with open(csv_path, 'w', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results_lst)
        print('written to csv')

class SearchPage():

    def __init__(self):
        self.advanced_ref_link_text = 'Advanced'
        self.search_field_id = 'searchfield'
        self.search_btn_id = 'advSearch'

    def search(self, query):
        '''
        Searches for sources, with given query
        in Scopus

        '''

        advanced_ref = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click Advanced Search
            EC.presence_of_element_located((By.LINK_TEXT, self.advanced_ref_link_text)))
        advanced_ref.click()

        search_field = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
            EC.visibility_of_element_located((By.ID, self.search_field_id)))
        search_field.clear()
        search_field.send_keys(query)

        search_btn = browser.find_element_by_id(self.search_btn_id)    # when query is sent, find & press the search button
        search_btn.click()

class DocumentPage():

    def __init__(self, thread, total_docs_signal, update_progress_bar_signal):
        self.percentile_categories_class_name = 'treeLineContainer'
        self.percentiles_xpath = '//*[contains(@class, "pull-left paddingLeftQuarter")]'
        self.metric_values_xpath = "//*[contains(@class, 'value fontMedLarge lineHeight2 blockDisplay')]"
        self.paging_ul_class_name = 'pagination'
        self.doc_source_class_name = 'ddmDocSource'      
        self.search_results_table_id = 'srchResultsList'
        self.doc_title_class_name = 'ddmDocTitle'
        self.authors_list_class_name = 'ddmAuthorList'
        self.pub_year_class_name = 'ddmPubYr'
        self.docs_total_number = 'resultsCount'

        self.total_docs_update = total_docs_signal
        self.update_progress_bar = update_progress_bar_signal

        self.analysis_thread = thread

        self.stop = False

    def analyze_documents(self):

        '''
        Scans every source & gets its rating
        Saves all percentiles, average of percentiles and name of source
        in a dictionary, which is appended in a list of dictionaries (all sources)

        '''
        final_lst = []
        curr_page = 1   # begin with page 1
        
        no_of_pages = self.get_number_of_pages() # get total number of pages
        document_rows = self.get_document_rows() # get all document names
        author_rows = self.get_author_rows() # get all author names
        source_rows = self.get_source_rows()    # get all source names
        year_rows = self.get_year_rows() # get all years
        total_docs = self.get_total_number_of_docs()    # get the number of total docs
        self.total_docs_update.emit(total_docs)
        i=1
        while True:
            
            print(self.stop)
            if self.stop:
                return

            try:
                document_name = document_rows.popleft() # pop the first one in list
                author_list = author_rows.popleft()
                source_name = source_rows.popleft()
                year = year_rows.popleft()

                if source_name['clickable']:
                    source = WebDriverWait(browser, init.DELAY_TIME).until(    
                        EC.presence_of_element_located((By.LINK_TEXT, source_name['name'])))   # go in document's page
                    browser.execute_script("arguments[0].click();", source) # javascript click

                    try:
                        categories = WebDriverWait(browser, init.DELAY_TIME).until(    
                            EC.presence_of_all_elements_located((By.CLASS_NAME, self.percentile_categories_class_name)))    # find categories names

                        categories = self.convert_to_txt(categories) # convert categories from web element to string

                        try:
                            percentiles = WebDriverWait(browser, init.DELAY_TIME).until(    
                                EC.presence_of_all_elements_located((By.XPATH, self.percentiles_xpath))) # find percentiles

                            percentiles = self.percentiles_to_num(self.convert_to_txt(percentiles))   # convert percentiles to number (int)

                            print(percentiles)

                        except:
                            print('no percentiles found')

                        try:

                            # metric_values = WebDriverWait(browser, DELAY_TIME).until(    
                            #     EC.presence_of_all_elements_located((By.XPATH, self.metric_values_xpath))) # find metrics (num)

                            # metric_values = self.convert_to_txt(metric_values)

                            try:
                                citescore_element = WebDriverWait(browser, init.DELAY_TIME).until(    
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="rpCard"]/h2/span')))

                                citescore = citescore_element.text
                            except:
                                citescore = 0

                            try:
                                sjr_element = WebDriverWait(browser, init.DELAY_TIME).until(    
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="sjrCard"]/h2/span')))
                                
                                sjr = sjr_element.text
                            except:
                                sjr = 0

                            try:
                                snip_element = WebDriverWait(browser, init.DELAY_TIME).until(    
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="snipCard"]/h2/span')))

                                snip = snip_element.text
                            except:
                                snip = 0

                            metric_values = [citescore, sjr, snip]
                        
                        except:
                            print('no metric values found')

                        document_dict = self.create_dict(i, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), self.get_average_percentile(percentiles), zip(['CiteScore', 'SJR', 'SNIP'], metric_values))

                        final_lst.append(document_dict)

                        print(document_dict)

                        self.update_progress_bar.emit(i)

                        i+=1

                        browser.execute_script("window.history.go(-1)") # go to the previous page
                    except:
                        document_dict = self.create_dict(i, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), 0, zip(['CiteScore', 'SJR', 'SNIP'], [0, 0, 0]))
                        final_lst.append(document_dict)
                        self.update_progress_bar.emit(i)
                        i+=1
                        print(document_dict)
                        browser.execute_script("window.history.go(-1)") # go to the previous page
                else:
                    document_dict = self.create_dict(i, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), 0, zip(['CiteScore', 'SJR', 'SNIP'], [0, 0, 0]))
                    final_lst.append(document_dict)
                    self.update_progress_bar.emit(i)
                    i+=1
                    print(document_dict)
            except:
                try:
                    if curr_page < no_of_pages:
                        curr_page = self.change_page(curr_page)  # change page
                        document_rows = self.get_document_rows() # get all document names
                        author_rows = self.get_author_rows() # get all author names
                        source_rows = self.get_source_rows()    # get all source names
                        year_rows = self.get_year_rows() # get all years
                    else:
                        break
                except:
                    break

        return final_lst

    def stop_analysis(self):
        self.stop = True

    def remove_digits(self, lst): 
        '''
        Takes a list of strings and
        removes digits from every element
        '''
        pattern = '[0-9]'
        lst = [re.sub(pattern, '', i) for i in lst]
        return lst

    def remove_spaces(self, lst):
        '''
        Takes a list of strings and
        removes spaces from every element
        '''
        lst = [x.strip(' ') for x in lst]
        return lst

    def remove_new_line(self, lst):
        '''
        Takes a list of strings and
        removes spaces from every element
        '''
        lst = [x.strip('\n.') for x in lst]
        return lst

    def create_dict(self, i, doc_name, source_name, year, authors, num_of_authors, avg_percentile, metrics):
        '''
        Takes some lists & a dictionary with info
        and creates a dictionary for each document with
        all the info needed
        '''
        dictionary = {'#': i, 'Document Name': doc_name, 'Source Name': source_name, 'Year': year, 'Authors': authors, '# Authors': num_of_authors, 'Average Percentile': avg_percentile}
        dictionary.update(metrics)
        return dictionary

    def get_number_of_authors(self, authors):
        '''
        Takes a string (author names) & returns
        an integer (total number of document's authors)
        '''
        split_authors = authors.split(',')
        return len([','.join(i) for i in zip(split_authors[::2], split_authors[1::2])])

    def convert_to_txt(self, lst):
        '''
        Takes a list of web elements & returns
        a list of strings (the string of each element)
        '''
        return [element.text for element in lst]

    def percentiles_to_num(self, lst):
        '''
        Takes a list of strings and takes the numbers
        from each element (percentiles). Returns a list of nums.
        '''
        percentiles_num = []
        for percentile in lst:
            percentiles_num.append(int(re.findall("\d+", percentile)[0]))
        return percentiles_num

    def get_average_percentile(self, percentiles):
        '''
        Takes a list of numbers (percentiles) 
        and returns their average
        '''
        average = float(sum(percentiles) / len(percentiles))
        return round(average, 2)

    def change_page(self, curr_page):
        '''
        Takes a number of page (int) and finds the next page
        If a next page is found, goes to next page
        If not, script exits (no other pages left)
        Returns the new curr_page
        '''
        try:
            paging_ul = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                EC.presence_of_element_located((By.CLASS_NAME, self.paging_ul_class_name)))
            pages = paging_ul.find_elements_by_tag_name('li')

            next_page = next(page for page in pages if page.text == str(curr_page+1))

            next_page.click()

            return curr_page+1

        except:
            print('error')

    def get_number_of_pages(self):
        '''
        Returns total number of pages
        '''
        paging_ul = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                EC.presence_of_element_located((By.CLASS_NAME, self.paging_ul_class_name)))
        return int(paging_ul.find_element_by_id("endPage").get_attribute("value"))

    def get_number_of_rows(self):
        '''
        Returns the number of rows
        of a page (number of documents)
        '''
        elements = []
        i=0
        while True:
            try:
                elements.append(browser.find_element_by_xpath('//*[@id="resultDataRow'+str(i)+'"]'))
                i+=1
            except:
                break
        return len(elements)

    def get_total_number_of_docs(self):
        '''
        Returns the total number of documents (that will be scanned)
        Used for scan dialog's progress bar
        '''
        total_docs_num = browser.find_element(By.CLASS_NAME, self.docs_total_number)
        return int(total_docs_num.text)

    def get_source_rows(self):
        '''
        Fetches all sources (names)
        and returns a string queue (with all the names)
        '''
        rows = []

        no_of_rows = self.get_number_of_rows()    # number of rows of current page

        i=1
        while i<=no_of_rows:
            td = WebDriverWait(browser, init.DELAY_TIME).until(    
                EC.presence_of_element_located((By.XPATH, '//*[@id="resultDataRow'+str(i-1)+'"]/td[4]'))) 
            try:
                row = td.find_element(By.CLASS_NAME, self.doc_source_class_name)
                rows.append({'name': row.text, 'clickable': True})
                i+=1
            except:
                rows.append({'name': td.text.splitlines()[0], 'clickable': False})
                i+=1

        return deque(rows)

    def get_document_rows(self):
        '''
        Fetches all documents (names)
        and returns a string queue (with all the names)
        '''
        results = WebDriverWait(browser, init.DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.doc_title_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

    def get_author_rows(self):
        '''
        Fetches all authors (names)
        and returns a string queue (with all the names)
        '''
        results = WebDriverWait(browser, init.DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.authors_list_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

    def get_year_rows(self):
        '''
        Fetches all years
        and returns a string queue (with all the years)
        '''
        results = WebDriverWait(browser, init.DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.pub_year_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)
