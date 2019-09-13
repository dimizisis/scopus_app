from PyQt5 import QtCore, QtGui, QtWidgets

from pyqtspinner.spinner import WaitingSpinner

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class WaitingDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
        self.title = "Processing..."
        self.setWindowTitle(self.title)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.spinner = WaitingSpinner(self)
        self.formLayout.addWidget(self.spinner)
        self.spinner.start()
        self.show()

    def close(self):
        self.close()
