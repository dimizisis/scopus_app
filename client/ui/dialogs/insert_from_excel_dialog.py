
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
import database.db as db
import sys
sys.path.append('../../')
import os

class Ui_InsertFromExcelDialog(object):

    ICON_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/favicon.ico'

    def setupUi(self, InsertFromExcelDialog):
        self.InsertFromExcelDialog = InsertFromExcelDialog
        self.InsertFromExcelDialog.setObjectName('InsertFromExcelDialog')
        self.InsertFromExcelDialog.resize(485, 227)
        self.InsertFromExcelDialog.setMaximumSize(QtCore.QSize(485, 227))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.InsertFromExcelDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 471, 211))
        self.verticalLayoutWidget.setObjectName('verticalLayoutWidget')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName('verticalLayout')
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName('add_btn')
        self.add_btn.setIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/branch-closed_hover.png'))
        self.add_btn.clicked.connect(self.open_file_dialog)
        self.horizontalLayout.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_btn.setObjectName('remove_btn')
        self.remove_btn.setIcon(QIcon(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + '../style/images/branch-open_hover.png'))
        self.remove_btn.clicked.connect(self.remove_selected_items)
        self.horizontalLayout.addWidget(self.remove_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName('listWidget')
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.verticalLayout.addWidget(self.listWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.accepted.connect(self.add_data_to_db)
        self.buttonBox.rejected.connect(self.InsertFromExcelDialog.close)
        self.verticalLayout.addWidget(self.buttonBox)
        self.retranslateUi(InsertFromExcelDialog)
        self.InsertFromExcelDialog.setWindowIcon(QIcon(self.ICON_PATH))
        QtCore.QMetaObject.connectSlotsByName(InsertFromExcelDialog)

    def retranslateUi(self, InsertFromExcelDialog):
        _translate = QtCore.QCoreApplication.translate
        self.InsertFromExcelDialog.setWindowTitle(_translate('InsertFromExcelDialog', 'Insert Data From Excel File(s)'))

    def open_file_dialog(self):
        '''
        When user hits the add button,
        a dialog appears, in order the user to choose excel file
        When ok is clicked, file's path is added to list widget
        '''
        filenames = QFileDialog.getOpenFileNames(None, 'Open', '', 'Excel Files (*.xlsx *.xls)')
        for filename in filenames[0]:
            self.listWidget.addItem(filename)

    def remove_selected_items(self):
        '''
        Removes selected items from list
        Triggered when the minus (-) button is clicked
        '''
        list_items = self.listWidget.selectedItems()
        if not list_items: return
        for item in list_items:
            self.listWidget.takeItem(self.listWidget.row(item))
    
    def add_data_to_db(self):
        filenames = list()
        for i in range(self.listWidget.count()-1):
            filenames.append(self.listWidget.item(i).text())
        
        if filenames:
            success = db.insert_from_excel(filenames)

            if success:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('All files are successfully added to database.')
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.setWindowIcon(QIcon(self.ICON_PATH))
                msg.setWindowTitle('Success!')
                msg.exec_()
                self.InsertFromExcelDialog.close()

        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('No excel files are selected.')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setWindowIcon(QIcon(self.ICON_PATH))
            msg.setWindowTitle('Something went wrong!')
            msg.exec_()
            self.InsertFromExcelDialog.close()
