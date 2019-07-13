# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nikzi\Desktop\login_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import sys
from threading import Thread
import global_vars

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 276)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 401, 221))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 371, 184))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.email_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.email_label.setObjectName("email_label")
        self.horizontalLayout.addWidget(self.email_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.email_txt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email_txt.setObjectName("email_txt")
        self.horizontalLayout.addWidget(self.email_txt)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pass_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pass_label.setObjectName("pass_label")
        self.horizontalLayout_2.addWidget(self.pass_label)
        spacerItem2 = QtWidgets.QSpacerItem(2, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pass_txt = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.pass_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_txt.setObjectName("pass_txt")
        self.horizontalLayout_2.addWidget(self.pass_txt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.login_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_2.addWidget(self.login_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.login_btn.clicked.connect(self.login_btn_function)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.email_label.setText(_translate("MainWindow", "E-mail:"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Click to exit the app"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

    def login_btn_function(self):
        self.thread = LoginThread(parent=None, email=self.email_txt.text(), password=self.pass_txt.text())
        self.thread.start()
        self.login_btn.setEnabled(False)

class LoginPage():

    def __init__(self, browser):
        self.browser = global_vars.browser
        self.username_box_id = 'username'
        self.password_box_id = 'password-input-password'
        self.login_btn_xpath = '//*[@title="Login"]'
        self.document_header_xpath = '//h1[@class="documentHeader"]'

    def login(self, username, password):

        '''
        With given username & pass (credentials)
        logs in Scopus system

        '''

        url = 'https://www.scopus.com/customer/authenticate/loginfull.uri'

        self.browser.get((url))
        
        user_element = self.browser.find_element_by_id(self.username_box_id)   # Find the textboxes we'll send the credentials
        pass_element = self.browser.find_element_by_id(self.password_box_id)

        user_element.send_keys(username)    # send credentials to textboxes 
        pass_element.send_keys(password) 
        login_btn = self.browser.find_element_by_xpath(self.login_btn_xpath)    # find & click login button
        login_btn.click()

        try:
            # if document search text appears, login successful
            document_search_txt = WebDriverWait(self.browser, 6).until(EC.presence_of_element_located((By.XPATH, self.document_header_xpath)))
            print('Login ok')
        except:
            print('Login failed, program exiting now...')
            self.browser.close()
            exit(1)

class LoginThread(QtCore.QThread):

    signal = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, email='', password=''):
        super(LoginThread, self).__init__(parent)
        self.email = email
        self.passsword = password

    # run method gets called when we start the thread
    def run(self):
        login_page = LoginPage(None)
        login_page.login(self.email, self.passsword)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
