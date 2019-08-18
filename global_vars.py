from selenium import webdriver
import threading

DELAY_TIME = 10

login_url = 'https://www.scopus.com/customer/authenticate.uri'

search_url = 'https://www.scopus.com/search/form.uri?display=advanced'

options = webdriver.ChromeOptions()

# options.add_argument('headless') ## to be enabled later

browser = webdriver.Chrome(chrome_options=options, executable_path='C:/Users/nikzi/Desktop/Thesis/chromedriver.exe')

browser.get(login_url)