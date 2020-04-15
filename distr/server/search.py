from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import init

class SearchPage():

    def __init__(self):
        self.advanced_ref_link_text = 'Advanced'
        self.search_field_id = 'searchfield'
        self.search_btn_id = 'advSearch'
        self.close_window_id = '_pendo-close-guide_'
        self.results_lst_id = 'srchResultsList'

    def search(self, query, sio, browser):
        '''
        Searches for sources, with given query
        in Scopus
        '''
        window_showed = False

        try:
            # pop up window that appears in some occasions
            close_window_btn = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, self.close_window_id)))
            close_window_btn.click()
            window_showed = True
        except:
            print('No window showed.')
        
        advanced_ref = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click Advanced Search
            EC.presence_of_element_located((By.LINK_TEXT, self.advanced_ref_link_text)))
        advanced_ref.click()

        search_field = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
            EC.visibility_of_element_located((By.ID, self.search_field_id)))
        search_field.clear()
        search_field.send_keys(query)

        search_btn = browser.find_element_by_id(self.search_btn_id)    # when query is sent, find & press the search button
        search_btn.click()

        if not window_showed:
            try:
                # pop up window that appears in some occasions
                close_window_btn = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, self.close_window_id)))
                close_window_btn.click()
            except:
                print('No window showed.')

        try:
            results_lst = WebDriverWait(browser, init.DELAY_TIME).until(    # when page is loaded, click query text box & send our query
            EC.visibility_of_element_located((By.ID, self.results_lst_id)))
            # sio.emit(event='search_response', data='ok', namespace='/desktop_client')
            print('emitted ok')
            return 'ok'
        except Exception:
            print('error')
            sio.emit(event='search_response', data='error', namespace='/desktop_client')
