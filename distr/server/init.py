
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver_path = os.path.dirname(os.path.realpath(__file__)) + '\driver\chromedriver.exe'
import zipfile

DELAY_TIME = 60

login_url = 'https://www.scopus.com/'

search_url = 'https://www.scopus.com/search/form.uri?display=advanced'

def create_plugin():
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

def reset_browser(browser):
    # options = Options()
    # options.add_extension(create_plugin())
    # options.add_argument('--no-proxy-server')
    # options.add_argument("--start-maximized")
    # capabilities = options.to_capabilities()
    # user_agent = str(browser.execute_script("return navigator.userAgent;")).replace('Headless','')  # remove headless from user-agent (if headless is detected by site, our requests will be denied)
    # browser.close() # close browser with old user-agent
    # options.add_argument('user-agent={0}'.format(user_agent))   # update the user agent
    # browser = webdriver.Remote(session_id=session_id, command_executor=url, desired_capabilities=capabilities)
    # browser = webdriver.Chrome(executable_path=driver_path, port=int(url.split(':')[2]), options=options)
    # browser.session_id = session_id
    browser.delete_all_cookies()
    browser.get(search_url)
    return browser

def init_browser():
    options = Options()
    options.add_extension(create_plugin())
    options.add_argument('--no-proxy-server')
    # options.add_argument("--start-maximized")
    # user_agent = str(browser.execute_script("return navigator.userAgent;")).replace('Headless','')  # remove headless from user-agent (if headless is detected by site, our requests will be denied)
    # browser.close() # close browser with old user-agent
    # options.add_argument('user-agent={0}'.format(user_agent))   # update the user agent
    browser = webdriver.Chrome(options=options, executable_path=driver_path)    # open browser with new user agent
    browser.get(search_url)
    return browser