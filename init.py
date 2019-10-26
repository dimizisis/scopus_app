
import zipfile
from PyQt5 import QtWidgets, QtCore
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import login
import ctypes
import menu

DELAY_TIME = 60

LOGIN_DELAY_TIME = 60

login_url = 'https://www.scopus.com/'

search_url = 'https://www.scopus.com/search/form.uri?display=advanced'

driver_path = os.path.dirname(os.path.realpath(__file__)) + '\driver\chromedriver.exe'

browser = None

# icon init
myappid = 'uom.scopus.scopusanalyzer.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def update_browser(updated_browser):
    '''
    QThread changes the variable "browser", as the session id is changing
    This function is triggered when the QThread (BrowserThread) is finished and
    updates the global variable "browser" with the latest form.
    This function also updates the other global variables from other modules (2 function callings, in 2 forms we are going to need browser)
    '''
    global browser
    browser = updated_browser

    login.update_browser(browser)   # one call for login form
    menu.update_browser(browser)    # the other call for menu

class BrowserThread(QtCore.QThread):
    '''
    In this thread the browser (driver) is initialized and
    we give the options (headless and user-agent change to bypass access issues)
    When thread is complete, login form shows up
    '''

    browser_change = QtCore.pyqtSignal(object)

    def __init__(self, parent=None, splash=None):
        super().__init__(parent=parent)
        self.splash = splash

    def create_plugin(self):
        manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "195.251.214.183",
                    port: parseInt(3128)
                },
                bypassList: ["foobar.com"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "dai17053",
                    password: "paokfc4."
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """


        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        return pluginfile

    def run(self):

        pluginfile = self.create_plugin()   # for proxy server
        
        options = Options()
        # options.headless = True   # to be enabled

        options.add_extension(pluginfile)

        global browser

        browser = webdriver.Chrome(options=options, executable_path=driver_path)

        user_agent = str(browser.execute_script("return navigator.userAgent;")).replace('Headless','')  # remove headless from user-agent (if headless is detected by site, our requests will be denied)

        browser.close() # close browser with old user-agent

        options.add_argument('user-agent={0}'.format(user_agent))   # update the user agent

        browser = webdriver.Chrome(options=options, executable_path=driver_path)    # open browser with new user agent

        browser.get(login_url)

        try:
            
            error = browser.find_element_by_id('errorPages')    # if page not found, reopen the browser until we have the login form

            while error is not None:

                browser.close()

                browser = webdriver.Chrome(options=options, executable_path=driver_path)

                browser.get(login_url)

                error = browser.find_element_by_id('errorPages')

            self.splash.close()

        except:
            self.splash.close()
        
        self.browser_change.emit(browser)
