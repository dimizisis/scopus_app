
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from queue import deque
import re
import init

class DocumentPage():
    def __init__(self):
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
        self.stop = False
        self.count = 0

    def analyze_documents(self, sio, browser, final_lst):
        '''
        Scans every source & gets its rating
        Saves all percentiles, average of percentiles and name of source
        in a dictionary, which is appended in a list of dictionaries (all sources)
        '''
        curr_page = 1   # begin with page 1
        
        no_of_pages = self.get_number_of_pages(browser) # get total number of pages
        document_rows = self.get_document_rows(browser) # get all document names
        author_rows = self.get_author_rows(browser) # get all author names
        source_rows = self.get_source_rows(browser)    # get all source names
        year_rows = self.get_year_rows(browser) # get all years
        total_docs = self.get_total_number_of_docs(browser)    # get the number of total docs
        # sio.emit(event='total_docs', data=total_docs, namespace='/desktop_client')
        self.count=1
        while True:
            
            if self.stop == True:
                break
            try:
                document_name = document_rows.popleft() # pop the first one in list
                author_list = author_rows.popleft()
                source_name = source_rows.popleft()
                year = year_rows.popleft()

                doc_dict = next((src for src in final_lst if src['Source Name'] == source_name), None)

                if doc_dict is not None:
                    document_dict = self.create_dict(self.count, document_name, doc_dict['Source Name'], year, author_list, 
                                        self.get_number_of_authors(author_list), doc_dict['Average Percentile'], zip(['CiteScore', 'SJR', 'SNIP'], [doc_dict['CiteScore'], doc_dict['SJR'], doc_dict['SNIP']]))
                    final_lst.append(document_dict)
                    self.count+=1
                    continue

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
                        except Exception as e:
                            print(e)
                        try:
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
                        except Exception as e1:
                            print(e1)
                        document_dict = self.create_dict(self.count, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), self.get_average_percentile(percentiles), zip(['CiteScore', 'SJR', 'SNIP'], metric_values))
                        final_lst.append(document_dict)
                        self.count+=1
                        browser.execute_script("window.history.go(-1)") # go to the previous page
                    except:
                        document_dict = self.create_dict(self.count, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), 0, zip(['CiteScore', 'SJR', 'SNIP'], [0, 0, 0]))
                        final_lst.append(document_dict)
                        self.count+=1
                        browser.execute_script("window.history.go(-1)") # go to the previous page
                else:
                    document_dict = self.create_dict(self.count, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), 0, zip(['CiteScore', 'SJR', 'SNIP'], [0, 0, 0]))
                    final_lst.append(document_dict)
                    self.count+=1
                print(document_dict)
            except:
                try:
                    if curr_page < no_of_pages:
                        curr_page = self.change_page(curr_page, browser)  # change page
                        document_rows = self.get_document_rows(browser) # get all document names
                        author_rows = self.get_author_rows(browser) # get all author names
                        source_rows = self.get_source_rows(browser)    # get all source names
                        year_rows = self.get_year_rows(browser) # get all years
                    else:
                        break
                except:
                    break

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
        dictionary = {'Document Name': doc_name, 'Source Name': source_name, 'Year': year, 'Authors': authors, '# Authors': num_of_authors, 'Average Percentile': avg_percentile}
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

    def change_page(self, curr_page, browser):
        '''
        Takes a number of page (int) and finds the next page
        If a next page is found, goes to next page
        If not, script exits (no other pages left)
        Returns the new curr_page
        '''
        try:
            paging_ul = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                EC.visibility_of_element_located((By.CLASS_NAME, self.paging_ul_class_name)))
            pages = paging_ul.find_elements_by_tag_name('li')

            next_page = next(page for page in pages if page.text == str(curr_page+1))

            try:
                next_page.click()
            except Exception as e:
                print(e)
                WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                    EC.element_to_be_clickable((By.LINK_TEXT, next_page.text)))
                next_page.click()

            return curr_page+1

        except Exception as e:
            print(e)

    def get_number_of_pages(self, browser):
        '''
        Returns total number of pages
        '''
        paging_ul = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                EC.presence_of_element_located((By.CLASS_NAME, self.paging_ul_class_name)))
        return int(paging_ul.find_element_by_id("endPage").get_attribute("value"))

    def get_number_of_rows(self, browser):
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

    def get_total_number_of_docs(self, browser):
        '''
        Returns the total number of documents (that will be scanned)
        Used for scan dialog's progress bar
        '''
        total_docs_num = browser.find_element(By.CLASS_NAME, self.docs_total_number)
        return int(total_docs_num.text)

    def get_source_rows(self, browser):
        '''
        Fetches all sources (names)
        and returns a string queue (with all the names)
        '''
        rows = []

        no_of_rows = self.get_number_of_rows(browser)    # number of rows of current page

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

    def get_document_rows(self, browser):
        '''
        Fetches all documents (names)
        and returns a string queue (with all the names)
        '''
        results = WebDriverWait(browser, init.DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.doc_title_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

    def get_author_rows(self, browser):
        '''
        Fetches all authors (names)
        and returns a string queue (with all the names)
        '''
        results = WebDriverWait(browser, init.DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.authors_list_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

    def get_year_rows(self, browser):
        '''
        Fetches all years
        and returns a string queue (with all the years)
        '''
        results = WebDriverWait(browser, init.DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.pub_year_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)
