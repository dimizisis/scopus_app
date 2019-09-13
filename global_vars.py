from selenium import webdriver
import threading
from waiting_dialog import WaitingDialog
from PyQt5 import QtWidgets
import sys

DELAY_TIME = 10

login_url = 'https://www.scopus.com/customer/authenticate.uri'

search_url = 'https://www.scopus.com/search/form.uri?display=advanced'

options = webdriver.ChromeOptions()

# options.add_argument('headless') ## to be enabled later

# app = QtWidgets.QApplication(sys.argv)

# dialog = WaitingDialog()

browser = webdriver.Chrome(chrome_options=options, executable_path='')

browser.get(login_url)

try:
    error = browser.find_element_by_id('errorPages')

    while error is not None:

        browser.close()

        browser = webdriver.Chrome(chrome_options=options, executable_path='')

        browser.get(login_url)

        error = browser.find_element_by_id('errorPages')

    # dialog.close()

except:
    pass
    # dialog.close()