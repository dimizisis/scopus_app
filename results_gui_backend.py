# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nikzi\Desktop\results_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow, results):
        self.ResultsWindow = ResultsWindow
        self.results = results
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(833, 342)
        ResultsWindow.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.centralwidget = QtWidgets.QWidget(ResultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(10, 270, 101, 31))
        self.back_btn.setObjectName("back_btn")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 811, 241))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.statistics_btn = QtWidgets.QPushButton(self.centralwidget)
        self.statistics_btn.setGeometry(QtCore.QRect(720, 270, 101, 31))
        self.statistics_btn.setObjectName("statistics_btn")
        ResultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ResultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ResultsWindow)
        self.statusbar.setObjectName("statusbar")
        ResultsWindow.setStatusBar(self.statusbar)
        self.actionBack = QtWidgets.QAction(ResultsWindow)
        self.actionBack.setObjectName("actionBack")
        self.actionExit = QtWidgets.QAction(ResultsWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionBack)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(self.ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(self.ResultsWindow)

        row_count = (len(self.results))
        column_count = (len(self.results[0]))

        self.tableWidget.setColumnCount(column_count) 
        self.tableWidget.setRowCount(row_count)

        self.tableWidget.setHorizontalHeaderLabels((list(self.results[0].keys())))

        for row in range(row_count):  # add items from array to QTableWidget
            for column in range(column_count):
                item = (list(self.results[row].values())[column])
                if not isinstance(item, str):
                    item = str(item)
                self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(item))
                
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
