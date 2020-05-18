
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt
import os
import database.db as db
import sys
sys.path.append('../../')

class Ui_deleteDialog(object):
    def setupUi(self, deleteDialog):
        self.deleteDialog = deleteDialog
        self.deleteDialog.setObjectName('deleteDialog')
        self.deleteDialog.resize(288, 98)
        self.deleteDialog.setMaximumSize(QtCore.QSize(288, 98))
        self.deleteDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gridLayoutWidget = QtWidgets.QWidget(deleteDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 81))
        self.gridLayoutWidget.setObjectName('gridLayoutWidget')
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName('gridLayout')
        self.year_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.year_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.year_lbl.setStyleSheet('background-color: transparent')
        self.year_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.year_lbl.setObjectName('year_lbl')
        self.year_lbl.setAttribute(Qt.WA_NoSystemBackground)
        self.gridLayout.addWidget(self.year_lbl, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName('buttonBox')
        self.buttonBox.accepted.connect(self.perform_deletion)
        self.buttonBox.accepted.connect(self.deleteDialog.accept)
        self.buttonBox.rejected.connect(self.deleteDialog.close)
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMaximumSize(QtCore.QSize(237, 20))
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setObjectName('comboBox')
        self.comboBox.addItem('All')
        self.comboBox.addItems(self.fetch_years_from_db())
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.deleteDialog.setWindowIcon(QIcon(scriptDir + os.path.sep + '../style/images/favicon.ico')) 

        self.retranslateUi(deleteDialog)
        QtCore.QMetaObject.connectSlotsByName(deleteDialog)

    def retranslateUi(self, deleteDialog):
        _translate = QtCore.QCoreApplication.translate
        deleteDialog.setWindowTitle(_translate('deleteDialog', 'Delete from Database'))
        self.year_lbl.setText(_translate('deleteDialog', 'Year:'))    
    
    def fetch_years_from_db(self):
        import database.db as db
        return [str(year[0]) for year in db.get_distinct_years()]

    def perform_deletion(self):
        import database.db as db
        if self.comboBox.count() > 0:
            year = self.comboBox.currentText()
            success = db.perform_deletion(year) if year != 'All' else db.perform_deletion_all()
            return success
