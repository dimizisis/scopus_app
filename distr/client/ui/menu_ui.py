
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QFileDialog
import re
from pyqtspinner.spinner import WaitingSpinner
import magic
import os
from ui.dialogs.scan_dialog import Ui_ScanDialog

class ListView(QtWidgets.QListWidget):
    '''
    Custom ListView (QListWidget) in order
    to handle the drag & drop event (excel file addition)
    '''
    def __init__(self, parent=None):
        super(ListView, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setIconSize(QtCore.QSize(72, 72))

    def dragMoveEvent(self, event):
        pass

    def dragEnterEvent(self, e):
        '''
        If it is a file, we accept it
        '''
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):
        '''
        When a file is dropped, we check if it is ASCII text (excel)
        and if it is, it appears on the list
        Else, it is not accepted
        '''
        for url in e.mimeData().urls():
            if magic.from_file(url.toLocalFile()) == 'Microsoft Excel 2007+':
                self.addItem(url.toLocalFile())
            else:
                print(magic.from_file(url.toLocalFile()))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(750, 391)
        self.MainWindow.setMinimumSize(QtCore.QSize(750, 391))
        self.MainWindow.setMaximumSize(QtCore.QSize(750, 391))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinner = WaitingSpinner(self.MainWindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 731, 327))
        self.tabWidget.setStyleSheet("background-color: transparent;")
        self.tabWidget.setObjectName("tabWidget")
        self.new_search_tab = QtWidgets.QWidget()
        self.new_search_tab.setObjectName("new_search_tab")
        self.search_settings_grpbox = QtWidgets.QGroupBox(self.new_search_tab)
        self.search_settings_grpbox.setGeometry(QtCore.QRect(10, 10, 341, 260))
        self.search_settings_grpbox.setObjectName("search_settings_grpbox")
        self.search_settings_grpbox.setStyleSheet("background-color: transparent;")
        self.layoutWidget = QtWidgets.QWidget(self.search_settings_grpbox)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 30, 311, 225))
        self.layoutWidget.setObjectName("layoutWidget")
        self.search_settings_vertical_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.search_settings_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.search_settings_vertical_layout.setObjectName("search_settings_vertical_layout")
        self.uni_radio_btn = QtWidgets.QRadioButton(self.layoutWidget)
        self.uni_radio_btn.setEnabled(False)
        self.uni_radio_btn.setCheckable(True)
        self.uni_radio_btn.setChecked(True)
        self.uni_radio_btn.setAutoRepeat(False)
        self.uni_radio_btn.setObjectName("uni_radio_btn")
        self.search_settings_vertical_layout.addWidget(self.uni_radio_btn)
        self.year_horizontal_layout = QtWidgets.QHBoxLayout()
        self.year_horizontal_layout.setObjectName("year_horizontal_layout")
        self.year_label = QtWidgets.QLabel(self.layoutWidget)
        self.year_label.setObjectName("year_label")
        self.year_horizontal_layout.addWidget(self.year_label)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.year_horizontal_layout.addWidget(self.dateEdit)
        self.search_settings_vertical_layout.addLayout(self.year_horizontal_layout)
        self.src_type_horizontal_layout = QtWidgets.QHBoxLayout()
        self.src_type_horizontal_layout.setObjectName("src_type_horizontal_layout")
        self.src_type_label = QtWidgets.QLabel(self.layoutWidget)
        self.src_type_label.setObjectName("src_type_label")
        self.src_type_horizontal_layout.addWidget(self.src_type_label)
        spacerItem3 = QtWidgets.QSpacerItem(75, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.src_type_horizontal_layout.addItem(spacerItem3)
        self.src_type_combobox = QtWidgets.QComboBox(self.layoutWidget)
        self.src_type_combobox.setEnabled(True)
        self.src_type_combobox.setObjectName("src_type_combobox")
        self.src_type_combobox.addItem("Books")
        self.src_type_combobox.addItem("Book Series")
        self.src_type_combobox.addItem("Conference Proceedings")
        self.src_type_horizontal_layout.addWidget(self.src_type_combobox)
        self.doc_type_horizontal_layout = QtWidgets.QHBoxLayout()
        self.doc_type_horizontal_layout.setObjectName("doc_type_horizontal_layout")
        self.doc_type_label = QtWidgets.QLabel(self.layoutWidget)
        self.doc_type_label.setObjectName("doc_type_label")
        self.doc_type_label.setAlignment(QtCore.Qt.AlignTop)
        self.doc_type_horizontal_layout.addWidget(self.doc_type_label)
        self.doc_type_vertical_layout = QtWidgets.QVBoxLayout()
        self.doc_type_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.doc_type_vertical_layout.setObjectName("doc_type_vertical_layout")
        spacerItem2 = QtWidgets.QSpacerItem(10, 1, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.doc_type_vertical_layout.addItem(spacerItem2)
        self.article_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.article_checkbox.setChecked(True)
        self.article_checkbox.setObjectName("article_checkbox")
        self.doc_type_vertical_layout.addWidget(self.article_checkbox)
        self.review_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.review_checkbox.setChecked(True)
        self.review_checkbox.setObjectName("review_checkbox")
        self.doc_type_vertical_layout.addWidget(self.review_checkbox)
        self.editorial_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.editorial_checkbox.setChecked(True)
        self.editorial_checkbox.setObjectName("editorial_checkbox")
        self.doc_type_vertical_layout.addWidget(self.editorial_checkbox)
        self.conference_paper_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.conference_paper_checkbox.setChecked(True)
        self.conference_paper_checkbox.setObjectName("conference_paper_checkbox")
        self.doc_type_vertical_layout.addWidget(self.conference_paper_checkbox)
        self.undefined_checkbox = QtWidgets.QCheckBox(self.layoutWidget)
        self.undefined_checkbox.setChecked(True)
        self.undefined_checkbox.setObjectName("undefined_checkbox")
        self.doc_type_vertical_layout.addWidget(self.undefined_checkbox)
        self.doc_type_horizontal_layout.addLayout(self.doc_type_vertical_layout)
        self.search_settings_vertical_layout.addLayout(self.src_type_horizontal_layout)
        self.search_settings_vertical_layout.addLayout(self.doc_type_horizontal_layout)
        self.export_settings_grpbox = QtWidgets.QGroupBox(self.new_search_tab)
        self.export_settings_grpbox.setGeometry(QtCore.QRect(370, 10, 351, 221))
        self.export_settings_grpbox.setStyleSheet("background-color: transparent;")
        self.export_settings_grpbox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.export_settings_grpbox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 311, 105))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.export_settings_vertical_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.export_settings_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.export_settings_vertical_layout.setObjectName("export_settings_vertical_layout")
        self.save_to_db_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.save_to_db_checkbox.setChecked(True)
        self.save_to_db_checkbox.setObjectName("save_to_db_checkbox")
        self.export_settings_vertical_layout.addWidget(self.save_to_db_checkbox)
        self.export_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.export_checkbox.setChecked(True)
        self.export_checkbox.setObjectName("export_checkbox")
        self.export_checkbox.stateChanged.connect(self.export_excel_checkbox_function)
        self.export_settings_vertical_layout.addWidget(self.export_checkbox)
        self.select_export_path_horizontalLayout = QtWidgets.QHBoxLayout()
        self.select_export_path_horizontalLayout.setObjectName("select_export_path_horizontalLayout")
        self.select_export_path_horizontalLayout_without_btn = QtWidgets.QHBoxLayout()
        self.select_export_path_horizontalLayout_without_btn.setObjectName("select_export_path_horizontalLayout_without_btn")
        self.select_path_label = QtWidgets.QLabel(self.layoutWidget1)
        self.select_path_label.setObjectName("select_path_label")
        self.select_export_path_horizontalLayout_without_btn.addWidget(self.select_path_label)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.select_export_path_horizontalLayout_without_btn.addItem(spacerItem)
        self.export_path_textedit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.export_path_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_path_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_path_textedit.setReadOnly(True)
        self.export_path_textedit.setObjectName("export_path_textedit")
        self.select_export_path_horizontalLayout_without_btn.addWidget(self.export_path_textedit)
        self.select_export_path_horizontalLayout.addLayout(self.select_export_path_horizontalLayout_without_btn)
        self.path_select_toolbtn = QtWidgets.QToolButton(self.layoutWidget1)
        self.path_select_toolbtn.setObjectName("path_select_toolbtn")
        self.path_select_toolbtn.clicked.connect(self.open_directory_dialog)
        self.select_export_path_horizontalLayout.addWidget(self.path_select_toolbtn)
        self.export_settings_vertical_layout.addLayout(self.select_export_path_horizontalLayout)
        self.select_excel_filename_horizontal_layout = QtWidgets.QHBoxLayout()
        self.select_excel_filename_horizontal_layout.setObjectName("select_excel_filename_horizontal_layout")
        self.export_filename_label = QtWidgets.QLabel(self.layoutWidget1)
        self.export_filename_label.setObjectName("export_filename_label")
        self.select_excel_filename_horizontal_layout.addWidget(self.export_filename_label)
        self.export_filename_textedit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.export_filename_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_filename_textedit.setObjectName("export_filename_textedit")
        self.select_excel_filename_horizontal_layout.addWidget(self.export_filename_textedit)
        self.export_settings_vertical_layout.addLayout(self.select_excel_filename_horizontal_layout)
        self.proceed_btn_search = QtWidgets.QCommandLinkButton(self.new_search_tab)
        self.proceed_btn_search.clicked.connect(self.proceed_btn_search_function)
        self.proceed_btn_search.setGeometry(QtCore.QRect(620, 250, 101, 41))
        self.proceed_btn_search.setObjectName("proceed_btn_search")
        
        self.tabWidget.addTab(self.new_search_tab, "")
        self.import_tab = QtWidgets.QWidget()
        self.import_tab.setObjectName("import_tab")
        self.listWidget = ListView(self.import_tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 731, 201))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setObjectName("listWidget")
        self.add_btn = QtWidgets.QPushButton(self.import_tab)
        self.add_btn.setGeometry(QtCore.QRect(650, 10, 31, 23))
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.add_btn.setIcon(QIcon(scriptDir + os.path.sep + '\\style\\images\\branch-closed_hover.png'))
        self.add_btn.setObjectName("add_btn")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.clicked.connect(self.open_file_dialog)
        self.remove_btn = QtWidgets.QPushButton(self.import_tab)
        self.remove_btn.setGeometry(QtCore.QRect(690, 10, 31, 23))
        self.remove_btn.setIcon(QIcon(scriptDir + os.path.sep + 'style\\images\\branch-open_hover.png'))
        self.remove_btn.setObjectName("remove_btn")
        self.remove_btn.setFont(font)
        self.remove_btn.clicked.connect(self.remove_selected_items)
        self.proceed_btn_stats = QtWidgets.QCommandLinkButton(self.import_tab)
        self.proceed_btn_stats.setGeometry(QtCore.QRect(620, 250, 101, 41))
        self.proceed_btn_stats.setObjectName("proceed_btn_stats")
        self.tabWidget.addTab(self.import_tab, "")

        self.database_tab = QtWidgets.QWidget()
        self.database_tab.setObjectName("database_tab")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.database_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 711, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.database_table = QtWidgets.QTableWidget(self.database_tab)
        self.database_table.setSortingEnabled(True)
        self.database_table.setGeometry(QtCore.QRect(10, 10, 711, 221))
        self.database_table.setObjectName("database_table")
        self.database_table.setColumnCount(9)
        self.delete_db_btn = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.delete_db_btn.setGeometry(QtCore.QRect(10, 250, 185, 41))
        self.delete_db_btn.setObjectName("delete_db_btn")
        self.insert_db_btn = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.insert_db_btn.setObjectName("insert_db_btn")
        self.insert_db_btn.setIcon(QIcon(scriptDir + os.path.sep + 'style\\images\\insert.png'))
        # self.delete_db_btn.setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(120,120,120), stop: 1 rgb(80,80,80));')
        self.delete_db_btn.setIcon(QIcon(scriptDir + os.path.sep + 'style\\images\\delete.png'))
        self.delete_db_btn.clicked.connect(self.open_delete_from_db_dialog)
        self.db_export_stats_btn = QtWidgets.QCommandLinkButton(self.horizontalLayoutWidget)
        self.db_export_stats_btn.setGeometry(QtCore.QRect(540, 250, 185, 41))
        self.db_export_stats_btn.setObjectName("db_export_stats_btn")
        self.db_export_stats_btn.setIcon(QIcon(scriptDir + os.path.sep + 'style\\images\\export.png'))
        self.tabWidget.addTab(self.database_tab, "")
        self.load_data_from_db()

        self.db_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.db_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.db_horizontalLayout.setObjectName("db_horizontalLayout")
        self.db_horizontalLayout.addWidget(self.delete_db_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.db_horizontalLayout.addItem(spacerItem1)
        self.db_horizontalLayout.addWidget(self.insert_db_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.db_horizontalLayout.addItem(spacerItem2)
        self.db_horizontalLayout.addWidget(self.db_export_stats_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionExit.setObjectName("actionLogout")
        self.actionChangeTab = QtWidgets.QShortcut(QKeySequence("Ctrl+Tab"), MainWindow)
        self.actionChangeTab.activated.connect(self.change_tab)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.MainWindow.setWindowIcon(QIcon(scriptDir + os.path.sep + '\\style\\images\\favicon.ico')) 

        self.export_path = None

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScopusAnalyzer - Menu"))
        self.search_settings_grpbox.setTitle(_translate("MainWindow", "Search Settings"))
        self.uni_radio_btn.setText(_translate("MainWindow", "University Of Macedonia"))
        self.year_label.setText(_translate("MainWindow", "Year:"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.src_type_label.setText(_translate("MainWindow", "Source Type:"))
        self.doc_type_label.setText(_translate("MainWindow", "Document Type:"))
        self.src_type_combobox.setItemText(0, _translate("MainWindow", "Journals"))
        self.src_type_combobox.setItemText(1, _translate("MainWindow", "Conference Proceedings"))
        self.src_type_combobox.setItemText(2, _translate("MainWindow", "Book Series"))
        self.src_type_combobox.setItemText(3, _translate("MainWindow", "Books"))
        self.review_checkbox.setText(_translate("MainWindow", "Review"))
        self.article_checkbox.setText(_translate("MainWindow", "Article"))
        self.editorial_checkbox.setText(_translate("MainWindow", "Editorial"))
        self.conference_paper_checkbox.setText(_translate("MainWindow", "Conference Paper"))
        self.undefined_checkbox.setText(_translate("MainWindow", "Undefined"))
        self.export_settings_grpbox.setTitle(_translate("MainWindow", "Export Settings"))
        self.export_checkbox.setText(_translate("MainWindow", "Export results to excel"))
        self.select_path_label.setText(_translate("MainWindow", "Select Export Path:"))
        # self.export_path_textedit.setPlaceholderText(_translate("MainWindow", "Export Path..."))
        self.path_select_toolbtn.setText(_translate("MainWindow", "..."))
        self.export_filename_label.setText(_translate("MainWindow", "Select excel Filename:"))
        self.proceed_btn_search.setText(_translate("MainWindow", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_search_tab), _translate("MainWindow", "New Search"))
        self.proceed_btn_stats.setText(_translate("MainWindow", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.import_tab), _translate("MainWindow", "Import excels"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.remove_btn.setToolTip(_translate("MainWindow", "Remove excel from list"))
        self.add_btn.setToolTip(_translate("MainWindow", "Add excel"))
        self.save_to_db_checkbox.setText(_translate("MainWindow", "Save Results to Database"))

        self.delete_db_btn.setText(_translate("MainWindow", "Delete..."))
        self.insert_db_btn.setText(_translate("MainWindow", "Insert from Excel..."))
        self.db_export_stats_btn.setText(_translate("MainWindow", "Export Statistics"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.database_tab), _translate("MainWindow", "Database"))

    def change_tab(self):
        '''
        Changes current tab
        Triggered when CTRL+Tab is pressed
        '''
        desired_index = (self.tabWidget.currentIndex() + 1) % self.tabWidget.count()
        self.tabWidget.setCurrentIndex(desired_index)
    
    def load_data_from_db(self):

        import database.db as db

        self.database_table.setRowCount(0)
        
        rows = db.get_all_records()

        self.database_table.setHorizontalHeaderLabels(['Document Name', '# Authors', 'Authors', 'Year', 'Source Name', 'Average Percentile', 'CiteScore', 'SJR', 'SNIP'])

        for row in rows:
            inx = rows.index(row)
            self.database_table.insertRow(inx)
            for i in range(0, 9):
                if i != 7 and i != 8:
                    self.database_table.setItem(inx, i, QtWidgets.QTableWidgetItem(str(row[i])))
                else:
                    self.database_table.setItem(inx, i, QtWidgets.QTableWidgetItem(str(round(row[i], 3))))

    def open_delete_from_db_dialog(self):
        from ui.dialogs.delete_from_db_dialog import Ui_deleteDialog

        self.db_dialog = QtWidgets.QDialog()
        self.db_dialog.dialog_ui = Ui_deleteDialog()
        self.db_dialog.dialog_ui.setupUi(deleteDialog=self.db_dialog)
        self.db_dialog.exec_()

        self.load_data_from_db()

        return

    def proceed_btn_search_function(self):
        '''
        When user hits proceed button, a scan dialog appears,
        which shows the progress of the expected search (progress bar & percentage of completion)
        '''
        if self.export_checkbox.isChecked():
            if not self.export_path_textedit.toPlainText():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Please select a valid export path.")
                msg.setWindowTitle("Error")
                msg.exec_()
                return

            if not self.export_filename_textedit.toPlainText():
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText('Please enter a valid output filename.')
                msg.setWindowTitle("Error")
                msg.exec_()
                return
            if '.xlsx' not in self.export_filename_textedit.toPlainText() or '.xls' not in self.export_filename_textedit.toPlainText():
                self.export_path = self.export_path_textedit.toPlainText() + '/' + self.export_filename_textedit.toPlainText() + '.xlsx'
            else:
                self.export_path = self.export_path_textedit.toPlainText() + '/' + self.export_filename_textedit.toPlainText()

        self.dialog = QtWidgets.QDialog()
        self.dialog.dialog_ui = Ui_ScanDialog()
        success = self.dialog.dialog_ui.setupUi(self.dialog, self.MainWindow, self.generate_query(), self.export_checkbox.isChecked(), self.export_path, self.save_to_db_checkbox.isChecked())
        if success:
            self.dialog.exec_()

    def open_directory_dialog(self):
        '''
        When user hits the tool button,
        a dialog appears, in order the user to choose the folder
        in which the excel will be exported after the completion of search
        '''
        self.dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.export_path_textedit.setText(self.dir_)

    def open_file_dialog(self):
        '''
        When user hits the add button,
        a dialog appears, in order the user to choose excel file
        When ok is clicked, file's path is added to list widget
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filenames = QFileDialog.getOpenFileNames(None,"Open", "", 'Excel Files (*.xlsx *.xls)', options=options)
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

    def export_excel_checkbox_function(self):
        '''
        If user unchecks the "Export excel", then
        he will not be able to choose path or filename (because there will be no file)
        '''
        if not self.export_checkbox.isChecked():
            self.path_select_toolbtn.setEnabled(False)
            self.export_filename_textedit.setEnabled(False)
        else:
            self.path_select_toolbtn.setEnabled(True)
            self.export_filename_textedit.setEnabled(True)

    def generate_query(self):
        '''
        This function generates a specific search query
        according to user's choices (from menu UI)
        Returns the query (str)
        '''
        limits = []
        
        pub_year = self.dateEdit.text()
        limits.append(f'  AND  ( LIMIT-TO ( PUBYEAR ,  {pub_year} ) )')

        src_type = 'j' # by default

        if self.src_type_combobox.currentText() == 'Journals':
            src_type = 'j'
        elif self.src_type_combobox.currentText() == 'Books':
            src_type = 'b'
        elif self.src_type_combobox.currentText() == 'Book Series':
            src_type = 'k'
        elif self.src_type_combobox.currentText() == 'Conference Proceedings':
            src_type = 'p'
        limits.append(f'  AND  ( LIMIT-TO ( SRCTYPE ,  "{src_type}" )')

        if self.article_checkbox.isChecked():
            limits.append('  AND  ( LIMIT-TO ( DOCTYPE ,  "ar" ) ')
        if self.review_checkbox.isChecked():
            limits.append('  AND  LIMIT-TO ( DOCTYPE ,  "re" )')
        if self.conference_paper_checkbox.isChecked():
            limits.append('  AND  LIMIT-TO ( DOCTYPE ,  "cp" )')
        if self.editorial_checkbox.isChecked():
            limits.append('  AND  LIMIT-TO ( DOCTYPE ,  "ed" )')
        if self.undefined_checkbox.isChecked():
            limits.append('  AND  LIMIT-TO ( DOCTYPE ,  "Undefined" )')

        query = '( AF-ID ( "Panepistimion Makedonias"   60001086 ) )'

        for limit in limits:
            query += limit

        print(query)

        return query
