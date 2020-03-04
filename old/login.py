from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

import init

browser = None

def update_browser(updated_browser):
    '''
    Updates the browser with its latest form
    '''
    global browser
    browser = updated_browser

class LoginPage():

    def __init__(self):
        self.browser = browser
        self.username_box_id = 'username'
        self.password_box_id = 'password-input-password'
        self.login_btn_xpath = '//*[@title="Login"]'
        self.document_header_xpath = '//h1[@class="documentHeader"]'

        self.bdd_email_box_id = 'bdd-email'
        self.bdd_pass_box_id = 'bdd-password'
        self.bdd_login_btn_id = 'bdd-elsPrimaryBtn'
        self.sign_in_link_id = 'signin_link_move'
        self.close_window_id = '_pendo-close-guide_'

    def login(self, username, password):

        '''
        With given username & pass (credentials)
        logs in Scopus system

        '''

        try:
            # pop up window that appears in some occasions
            close_window_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, self.close_window_id)))
            close_window_btn.click()
        except:
            print('No window showed.')
        
        try:
            sign_in = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, self.sign_in_link_id)))
            sign_in.click()
        except:
            print('Logged out before')
        
        try:
            user_element = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, self.bdd_email_box_id))) # Find the textboxes we'll send the credentials
            user_element.clear()
            user_element.send_keys(username)    # send credentials to textboxes 
            continue_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, self.bdd_login_btn_id)))
            continue_btn.click()
            pass_element = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, self.bdd_pass_box_id)))
            pass_element.clear()
            pass_element.send_keys(password)    # send credentials to textboxes 
            login_btn = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, self.bdd_login_btn_id))) # find & click login button
            login_btn.click()
        except: # if we logged in before (in the same session), it asks only for password
            pass_element = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, self.bdd_pass_box_id)))
            pass_element.clear()
            pass_element.send_keys(password)    # send credentials to textboxes 
            login_btn = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, self.bdd_login_btn_id))) # find & click login button
            login_btn.click()
        try:
            # if document search text appears, login successful 
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, self.document_header_xpath)))
            print('Login ok')
            return True
        except:
            error = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'passworderror')))
            print('Login failed')
            self.browser.get(init.login_url)
            return False