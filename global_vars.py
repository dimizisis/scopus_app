from selenium import webdriver
import threading

login_url = 'https://www.scopus.com/customer/authenticate/loginfull.uri'

search_url = 'https://www.scopus.com/search/form.uri?display=advanced'

options = webdriver.ChromeOptions()

# options.add_argument('headless') ## to be enabled later

browser = webdriver.Chrome(chrome_options=options)

browser.get(login_url)