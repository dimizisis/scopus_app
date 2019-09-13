# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nikzi\Desktop\scan_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScanDialog(object):
    def setupUi(self, ScanDialog):
        ScanDialog.setObjectName("ScanDialog")
        ScanDialog.resize(440, 108)
        ScanDialog.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
        self.buttonBox = QtWidgets.QDialogButtonBox(ScanDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 70, 421, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.progressBar = QtWidgets.QProgressBar(ScanDialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 421, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(ScanDialog)
        self.buttonBox.accepted.connect(ScanDialog.accept)
        self.buttonBox.rejected.connect(ScanDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ScanDialog)

    def retranslateUi(self, ScanDialog):
        _translate = QtCore.QCoreApplication.translate
        ScanDialog.setWindowTitle(_translate("ScanDialog", "Scanning..."))
        self.progressBar.setFormat(_translate("ScanDialog", "%p%"))

