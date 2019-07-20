from selenium import webdriver
import threading

url = 'https://www.scopus.com/customer/authenticate/loginfull.uri'

options = webdriver.ChromeOptions()

# options.add_argument('headless') ## to be enabled later

browser = webdriver.Chrome(chrome_options=options, executable_path='C:/Users/nikzi/Desktop/Thesis/chromedriver.exe')

browser.get(url)