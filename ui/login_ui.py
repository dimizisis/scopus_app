
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from time import sleep
from init import DELAY_TIME, LOGIN_DELAY_TIME, login_url
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '\\images')
import img_source as img_source
import ui.menu_ui as menu_ui
import os
from pyqtspinner.spinner import WaitingSpinner
import login

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(851, 292)
        self.MainWindow.setMinimumSize(QtCore.QSize(851, 292))
        self.MainWindow.setMaximumSize(QtCore.QSize(851, 292))
        self.MainWindow.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
        self.MainWindow.setDocumentMode(False)
        self.MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(440, 0, 401, 251))
        self.groupBox.setObjectName("login_groupBox")
        self.groupBox.setStyleSheet("QGroupBox\n"
"{\n"
"  background-color: transparent;\n"
"  background-clip: margin;\n"
"  border: 1px solid rgb(20,20,20);\n"
"  border-radius: 4px;\n"
"  margin-top: 10px;\n"
"  padding-top: 4px;\n"
"}\n"
"\n"
"QGroupBox::title\n"
"{\n"
"  padding: 2px 8px;\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top center;\n"
"}\n"
"\n"
"QGroupBox::indicator\n"
"{\n"
"  border: 1px solid rgb(20,20,20);\n"
"  width: 14px;\n"
"  height: 14px;\n"
"}")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 371, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setStyleSheet("background-color: transparent;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.email_label = QtWidgets.QLabel(self.layoutWidget)
        self.email_label.setObjectName("email_label")
        self.email_label.setStyleSheet("background-color: transparent;")
        self.horizontalLayout.addWidget(self.email_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.email_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_txt.setObjectName("email_txt")
        self.horizontalLayout.addWidget(self.email_txt)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pass_label = QtWidgets.QLabel(self.layoutWidget)
        self.pass_label.setObjectName("pass_label")
        self.pass_label.setStyleSheet("background-color: transparent;")
        self.horizontalLayout_2.addWidget(self.pass_label)
        spacerItem2 = QtWidgets.QSpacerItem(2, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pass_txt = QtWidgets.QLineEdit(self.layoutWidget)
        self.pass_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pass_txt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_txt.setObjectName("pass_txt")
        self.horizontalLayout_2.addWidget(self.pass_txt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        self.login_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.setStyleSheet("QPushButton\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 darkslategray, stop: 1 rgb(80,80,80));\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(230,230,230);\n"
"  padding: 4px 8px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  border-color: rgb(90,200,255);\n"
"  padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"/**** QPushButton (checkable) ****/\n"
"QPushButton:checked\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(40,150,200), stop: 1 rgb(90,200,255));\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QPushButton:checked:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"}\n"
"\n"
"/**** QPushButton (disabled) ****/\n"
"QPushButton:disabled\n"
"{\n"
"  background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                    stop: 0 rgb(160,160,160), stop: 1 rgb(120,120,120));\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}")
        self.verticalLayout_2.addWidget(self.login_btn)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.login_failed_label = QtWidgets.QLabel(self.layoutWidget)
        self.login_failed_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_failed_label.setAutoFillBackground(False)
        self.login_failed_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.login_failed_label.setTextFormat(QtCore.Qt.RichText)
        self.login_failed_label.setScaledContents(False)
        self.login_failed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_failed_label.setWordWrap(False)
        self.login_failed_label.setObjectName("login_failed_label")
        self.verticalLayout.addWidget(self.login_failed_label)
        self.spinner = WaitingSpinner(self.MainWindow)
        self.verticalLayout.addWidget(self.spinner)
        self.scopus_image_label = QtWidgets.QLabel(self.centralwidget)
        self.scopus_image_label.setGeometry(QtCore.QRect(20, 10, 401, 241))
        self.scopus_image_label.setStyleSheet("image: url(:/scopus_logo/1280px-Scopus_logo.svg.png);\n"
"background-color: rgba(0,0,0,0%)")
        self.scopus_image_label.setText("")
        self.scopus_image_label.setObjectName("scopus_image_label")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(MainWindow.close)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.MainWindow.setWindowIcon(QIcon(scriptDir + os.path.sep + 'images\\favicon.ico')) 

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## My settings

        self.login_btn.clicked.connect(self.login_btn_function)
        self.login_btn.setShortcut('Return')
        self.login_failed_label.setVisible(False)

        self.email_txt.setText('dai17053@uom.edu.gr')
        self.pass_txt.setText('Uom53')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.groupBox.setTitle(_translate("MainWindow", "Login"))
        self.email_label.setText(_translate("MainWindow", "E-mail:"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.login_failed_label.setText(_translate("MainWindow", "Login Failed, please try again."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))

    def login_btn_function(self):

        '''
        Connecting ui with backend
        We create separated thread to perform the login (we want ui to be responsive during the login)

        '''
        self.spinner.start()
        self.login_failed_label.setVisible(False)
        self.thread = LoginThread(parent=None, email=self.email_txt.text(), password=self.pass_txt.text())
        self.thread.fail_signal.connect(self.login_failed_label.setVisible) # if login failed, show "login failed" to user
        self.thread.fail_signal.connect(self.spinner.stop)
        self.thread.fail_signal.connect(self.login_btn.setEnabled)  # if login failed, re-enable the login button in order the user tries again
        self.thread.open_menu_signal.connect(self.open_menu_window) # if login is successful, open menu window
        self.thread.start() # start the login thread
        self.login_btn.setEnabled(False)    # when user clicks login button, disable it

    def open_menu_window(self):

        '''
        When login successful, this function will be triggered (slot)
        to show the menu window (and "close" the login window)

        '''
        self.menu_ui = menu_ui.Ui_MainWindow()
        self.menu_ui.setupUi(self.MainWindow)
        self.MainWindow.show()
            
class LoginThread(QtCore.QThread):

    '''
    Login thread
    Performs the login in separated thread
    Email and password are typed by the user (ui text boxes)

    '''

    fail_signal = QtCore.pyqtSignal(bool)   # login failed signal
    open_menu_signal = QtCore.pyqtSignal()  # login success, signal menu window to open

    def __init__(self, parent=None, email='', password=''):
        super(LoginThread, self).__init__(parent)
        self.email = email
        self.passsword = password
        
    # run method gets called when we start the thread
    def run(self):
        login_page = login.LoginPage()
        success = login_page.login(self.email, self.passsword)
        if not success:
            self.fail_signal.emit(not success)
        else:
            self.open_menu_signal.emit()    # emit signal (to open the menu window)
