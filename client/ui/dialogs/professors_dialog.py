
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QAbstractItemView, Qt
import os
import sys
sys.path.append('../../')
import database.db as db

class Ui_Professors_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Ui_Professors_Dialog")
        Dialog.resize(318, 358)
        self.Dialog = Dialog
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.Dialog.setWindowIcon(QIcon(scriptDir + os.path.sep + '../style/images/favicon.ico')) 
        self.Dialog.setMaximumSize(QtCore.QSize(318, 358))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.tree_widget_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.tree_widget_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tree_widget_verticalLayout.setObjectName("tree_widget_verticalLayout")
        self.tree_widget = QtWidgets.QTreeWidget(self.verticalLayoutWidget)
        self.tree_widget.setColumnCount(3)
        self.tree_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tree_widget_verticalLayout.addWidget(self.tree_widget)
        self.select_deselect_all_horizontalLayout = QtWidgets.QHBoxLayout()
        self.select_deselect_all_horizontalLayout.setObjectName("select_deselect_all_horizontalLayout")
        self.deselect_all_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deselect_all_btn.setObjectName("deselect_all_btn")
        self.deselect_all_btn.clicked.connect(self.deselectAll)
        self.select_deselect_all_horizontalLayout.addWidget(self.deselect_all_btn)
        self.select_all_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.select_all_btn.setObjectName("select_all_btn")
        self.select_all_btn.clicked.connect(self.tree_widget.selectAll)
        self.select_deselect_all_horizontalLayout.addWidget(self.select_all_btn)
        self.tree_widget_verticalLayout.addLayout(self.select_deselect_all_horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 270, 91, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.ok_cancel_verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget_2.setAttribute(Qt.WA_NoSystemBackground)
        self.ok_cancel_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ok_cancel_verticalLayout.setObjectName("ok_cancel_verticalLayout")
        self.ok_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ok_btn.setObjectName("ok_btn")
        self.ok_cancel_verticalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.cancel_btn.setObjectName("cancel_btn")
        self.ok_cancel_verticalLayout.addWidget(self.cancel_btn)

        self.load_professors_from_db()

        self.ok_btn.clicked.connect(self.ok_pressed)
        self.cancel_btn.clicked.connect(self.Dialog.reject)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Select Professors", "Select Professors"))
        self.deselect_all_btn.setText(_translate("Dialog", "Deselect All"))
        self.select_all_btn.setText(_translate("Dialog", "Select All"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))

    def load_professors_from_db(self):
        rows = db.fetch_professors_from_db()
        self.tree_widget.setHeaderLabels(['Name', 'Surname', 'Department'])
        [self.tree_widget.addTopLevelItem(QtWidgets.QTreeWidgetItem([row[0], row[1], row[2]])) for row in rows]

    def ok_pressed(self):
        self.selected_professors = [{'Name': selected_prof.text(0), 'Surname': selected_prof.text(1), 'Department': selected_prof.text(2)} for selected_prof in self.tree_widget.selectedItems()]
        self.Dialog.accept()
    
    def deselectAll(self):
        for item in self.tree_widget.selectedItems():
            item.setSelected(False)
