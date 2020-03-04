
from PyQt5 import QtWidgets, QtCore
from pyqtspinner.spinner import WaitingSpinner
from PyQt5.QtGui import QPixmap, QIcon
import ui.login_ui as login_ui
import sys
import os
import init
import re

def show_splashscreen(splash):
    '''
    Shows splash screen when the program starts
    Splash screen is closed when login form is loaded (in browser)
    '''
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    splash.setWindowIcon(QIcon(scriptDir + os.path.sep + 'ui\\images\\favicon.ico')) 
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

def open_qss(path):
    """
    opens a Qt stylesheet with a path relative to the project

    Note: it changes the urls in the Qt stylesheet (in memory), and makes these urls relative to the project
    Warning: the urls in the Qt stylesheet should have the forward slash ('/') as the pathname separator
    """
    with open(path) as f:
        qss = f.read()
        pattern = r'url\((.*?)\);'
        for url in sorted(set(re.findall(pattern, qss)), key=len, reverse=True):
            directory, basename = os.path.split(path)
            new_url = os.path.join(directory, *url.split('/'))
            new_url = os.path.normpath(new_url)
            new_url = new_url.replace(os.path.sep, '/')
            qss = qss.replace(url, new_url)
        return qss

def show_login_screen():
    '''
    Just shows login screen when
    login form is completeley loaded in browser
    '''
    MainWindow.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qss = open_qss(os.path.dirname(os.path.abspath(__file__))+'\\ui\style\\stylesheet.qss')
    app.setStyleSheet(qss)
    splash = QtWidgets.QSplashScreen(QPixmap(), QtCore.Qt.WindowStaysOnTopHint)
    show_splashscreen(splash)
    browser_thread = init.BrowserThread(splash=splash)
    browser_thread.browser_change.connect(init.update_browser)
    browser_thread.finished.connect(show_login_screen)
    browser_thread.start()
    MainWindow = QtWidgets.QMainWindow()
    ui = login_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
