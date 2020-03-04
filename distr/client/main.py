
from PyQt5 import QtWidgets
import ui.menu_ui as menu_ui
import sys
import os
import re

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
    qss = open_qss(os.path.dirname(os.path.abspath(__file__))+'\\ui\style\\stylesheet.qss')
    app.setStyleSheet(qss)
    MainWindow = QtWidgets.QMainWindow()
    ui = menu_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
