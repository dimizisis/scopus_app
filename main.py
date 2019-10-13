from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from PyQt5 import QtWidgets, QtCore
from pyqtspinner.spinner import WaitingSpinner
from PyQt5.QtGui import QPixmap
import login_gui_backend
import sys
import zipfile

import login_gui_backend
import menu_gui_backend

DELAY_TIME = 60

LOGIN_DELAY_TIME = 60

login_url = 'https://www.scopus.com/'

search_url = 'https://www.scopus.com/search/form.uri?display=advanced'

driver_path = ''

browser = None

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

        # options.add_extension(pluginfile)

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


def show_splashscreen(splash):
    '''
    Shows splash screen when the program starts
    Splash screen is closed when login form is loaded (in browser)
    '''
    splash.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    splash.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
    title = "Processing..."
    splash.setWindowTitle(title)
    formLayoutWidget = QtWidgets.QWidget(splash)
    formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
    formLayoutWidget.setObjectName("formLayoutWidget")
    formLayout = QtWidgets.QFormLayout(formLayoutWidget)
    formLayout.setContentsMargins(0, 0, 0, 0)
    formLayout.setObjectName("formLayout")
    splash.setLayout(formLayout)
    spinner = WaitingSpinner(splash)
    formLayout.addWidget(spinner)
    spinner.start()
    splash.show()

def update_browser(updated_browser):
    '''
    QThread changes the variable "browser", as the session id is changing
    This function is triggered when the QThread (BrowserThread) is finished and
    updates the global variable "browser" with the latest form.
    This function also updates the other global variables from other modules (2 function callings, in 2 forms we are going to need browser)
    '''
    global browser
    browser = updated_browser

    login_gui_backend.update_browser(browser)   # one call for login form
    menu_gui_backend.update_browser(browser)    # the other call for menu

def show_login_screen():
    '''
    Just shows login screen when
    login form is completeley loaded in browser
    '''
    MainWindow.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QPixmap(), QtCore.Qt.WindowStaysOnTopHint)
    show_splashscreen(splash)
    browser_thread = BrowserThread(splash=splash)
    browser_thread.browser_change.connect(update_browser)
    browser_thread.finished.connect(show_login_screen)
    browser_thread.start()
    MainWindow = QtWidgets.QMainWindow()
    ui = login_gui_backend.Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
