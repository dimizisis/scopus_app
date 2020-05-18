
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import configparser
import network.proxy as proxy

def import_settings():
    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(os.path.realpath(__file__))+'/settings.ini')

    delay_time = parser.get('SYSTEM_SETTINGS', 'DELAY_TIME')
    search_url = parser.get('SYSTEM_SETTINGS', 'SEARCH_URL')
    driver_path = os.path.dirname(os.path.realpath(__file__)) + parser.get('SYSTEM_SETTINGS', 'WEBDRIVER_PATH')
    with_proxy = parser.get('SYSTEM_SETTINGS', 'PROXY')
    headless = parser.get('SYSTEM_SETTINGS', 'HEADLESS')

    return delay_time, search_url, driver_path, with_proxy, headless

DELAY_TIME = int(import_settings()[0])

search_url = import_settings()[1]

def init_browser():
    options = Options()
    with_proxy = import_settings()[3]
    headless = import_settings()[4]
    webdriver_path = import_settings()[2]

    if with_proxy.lower() == 'true':
        options.add_extension(proxy.create_plugin())
        options.add_argument('--no-proxy-server')

    elif headless.lower() == 'true':
        browser = webdriver.Chrome(options=options, executable_path=webdriver_path)
        user_agent = str(browser.execute_script("return navigator.userAgent;")).replace('Headless','')  # remove headless from user-agent (if headless is detected by site, our requests will be denied)
        browser.close() # close browser with old user-agent
        options.add_argument('user-agent={0}'.format(user_agent))   # update the user agent
        options.headless = True

    browser = webdriver.Chrome(options=options, executable_path=webdriver_path)    # open browser with new user agent
    browser.get(search_url)
    return browser
