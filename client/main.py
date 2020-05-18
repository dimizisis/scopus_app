
from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import Qt
from ui.menu_ui import Ui_MainWindow
import sys
import os
import re
import platform

if platform.system() == 'Windows':    # Windows
    # icon init
    import ctypes
    myappid = 'uom.scopus.scopusanalyzer.1' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def open_qss(path):
    """
    Opens a Qt stylesheet with a path relative to the project
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

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qss = open_qss(os.path.dirname(os.path.abspath(__file__))+'/ui/style/stylesheet.qss')
    app.setStyleSheet(qss)
    MainWindow = QtWidgets.QMainWindow()
    menu = Ui_MainWindow()
    menu.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
