# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nikzi\Desktop\results_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import ui.menu_ui as menu_ui
import pandas as pd
import os

class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow, lst):
        self.ResultsWindow = ResultsWindow
        self.results = lst[0]
        self.ResultsWindow.setObjectName("ResultsWindow")
        self.ResultsWindow.resize(833, 342)
        self.ResultsWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.ResultsWindow.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setStyleSheet("QPushButton\n"
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
        self.back_btn.setGeometry(QtCore.QRect(10, 270, 101, 31))
        self.back_btn.setObjectName("back_btn")
        self.back_btn.clicked.connect(self.go_to_menu)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 811, 241))
        self.tableWidget.setStyleSheet("QTableView\n"
"{\n"
"  alternate-background-color: rgb(110,110,110);\n"
"  background-color: rgb(100,100,100);\n"
"  border: 1px solid rgb(20,20,20);\n"
"  color: rgb(220,220,220);\n"
"  selection-background-color: rgb(70,110,130);\n"
"  selection-color: white;\n"
"}\n"
"\n"
"QTableView QLineEdit\n"
"{\n"
"  padding: -1 0 0 0;\n"
"}\n"
"\n"
"QTableView::item:hover,\n"
"QTableView::item:selected:hover\n"
"{\n"
"  background-color: rgb(70,110,130);\n"
"  color: white;\n"
"}\n"
"\n"
"QTableView::item:selected\n"
"{\n"
"  background-color: rgb(90,200,255);\n"
"  color: rgb(20,20,20);\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section\n"
"{\n"
"  background-color: rgb(60,60,60);\n"
"  border: 1px inset rgb(60,60,60);\n"
"}\n"
"\n"
"/**** QTableView (disabled) ****/\n"
"QTableView:disabled\n"
"{\n"
"  alternate-background-color: rgb(130,130,130);\n"
"  background-color: rgb(120,120,120);\n"
"  border-color: rgb(60,60,60);\n"
"  color: rgb(40,40,40);\n"
"}\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section:disabled\n"
"{\n"
"  background-color: rgb(80,80,80);\n"
"  border: 1px inset rgb(80,80,80);\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.statistics_btn = QtWidgets.QPushButton(self.centralwidget)
        self.statistics_btn.setStyleSheet("QPushButton\n"
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
        self.statistics_btn.setGeometry(QtCore.QRect(720, 270, 101, 31))
        self.statistics_btn.setObjectName("statistics_btn")
        self.ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.ResultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultsWindow)
        self.statusbar.setObjectName("statusbar")
        self.ResultsWindow.setStatusBar(self.statusbar)
        self.actionBack = QtWidgets.QAction(ResultsWindow)
        self.actionBack.setObjectName("actionBack")
        self.actionExit = QtWidgets.QAction(ResultsWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionBack)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.ResultsWindow.setWindowIcon(QIcon(scriptDir + os.path.sep + 'images\\favicon.ico')) 

        self.retranslateUi(self.ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(self.ResultsWindow)

        row_count = (len(self.results))
        column_count = (len(self.results[0]))

        self.tableWidget.setColumnCount(column_count) 
        self.tableWidget.setRowCount(row_count)

        self.tableWidget.setHorizontalHeaderLabels((list(self.results[0].keys())))

        for row in range(row_count):  # add items from array to QTableWidget
            for column in range(column_count):
                try:
                    item = (list(self.results[row].values())[column])
                    print(item)
                    if not isinstance(item, str):
                        item = str(item)
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(item))
                except:
                    print('Ok')
                
    def retranslateUi(self, ResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        ResultsWindow.setWindowTitle(_translate("ResultsWindow", "Analysis Results"))
        self.back_btn.setText(_translate("ResultsWindow", "Back"))
        self.statistics_btn.setText(_translate("ResultsWindow", "Show Stats"))
        self.menuFile.setTitle(_translate("ResultsWindow", "File"))
        self.actionBack.setText(_translate("ResultsWindow", "Back"))
        self.actionBack.setToolTip(_translate("ResultsWindow", "Back to menu"))
        self.actionBack.setShortcut(_translate("ResultsWindow", "Ctrl+B"))
        self.actionExit.setText(_translate("ResultsWindow", "Exit"))
        self.actionExit.setToolTip(_translate("ResultsWindow", "Exit application"))
        self.actionExit.setShortcut(_translate("ResultsWindow", "Ctrl+X"))

    def go_to_menu(self):

        '''
        When back button is clicked,
        the function will be executed
        in order to bring user back to
        main menu
        '''
        self.menu = menu_ui.Ui_MainWindow()
        self.menu.setupUi(self.ResultsWindow)
        self.ResultsWindow.show()
