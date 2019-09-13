# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nikzi\Desktop\menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from global_vars import browser, login_url, search_url, DELAY_TIME
from queue import deque
from threading import Thread
import login_gui_backend
import results_gui_backend
import magic

class ListView(QtWidgets.QListWidget):
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
        When a file is dropped, we check if it is ASCII text (CSV)
        and if it is, it appears on the list
        Else, it is not accepted
        '''
        for url in e.mimeData().urls():
            if magic.from_file(url.toLocalFile()) == 'ASCII text':
                self.addItem(url.toLocalFile())
            else:
                print(magic.from_file(url.toLocalFile()))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 391)
        self.MainWindow.setMinimumSize(QtCore.QSize(750, 391))
        self.MainWindow.setMaximumSize(QtCore.QSize(750, 391))
        self.MainWindow.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 731, 331))
        self.tabWidget.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.tabWidget.setObjectName("tabWidget")
        self.new_search_tab = QtWidgets.QWidget()
        self.new_search_tab.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.new_search_tab.setObjectName("new_search_tab")
        self.search_settings_grpbox = QtWidgets.QGroupBox(self.new_search_tab)
        self.search_settings_grpbox.setGeometry(QtCore.QRect(10, 10, 341, 221))
        self.search_settings_grpbox.setObjectName("search_settings_grpbox")
        self.layoutWidget = QtWidgets.QWidget(self.search_settings_grpbox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 311, 75))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uni_radio_btn = QtWidgets.QRadioButton(self.layoutWidget)
        self.uni_radio_btn.setEnabled(False)
        self.uni_radio_btn.setCheckable(True)
        self.uni_radio_btn.setChecked(True)
        self.uni_radio_btn.setAutoRepeat(False)
        self.uni_radio_btn.setObjectName("uni_radio_btn")
        self.verticalLayout.addWidget(self.uni_radio_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year_label = QtWidgets.QLabel(self.layoutWidget)
        self.year_label.setObjectName("year_label")
        self.horizontalLayout.addWidget(self.year_label)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.src_type_label = QtWidgets.QLabel(self.layoutWidget)
        self.src_type_label.setObjectName("src_type_label")
        self.horizontalLayout_2.addWidget(self.src_type_label)
        self.src_type_combobox = QtWidgets.QComboBox(self.layoutWidget)
        self.src_type_combobox.setEnabled(True)
        self.src_type_combobox.setObjectName("src_type_combobox")
        self.src_type_combobox.addItem("Books")
        self.src_type_combobox.addItem("Book Series")
        self.src_type_combobox.addItem("Conference Proceedings")
        self.horizontalLayout_2.addWidget(self.src_type_combobox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.export_settings_grpbox = QtWidgets.QGroupBox(self.new_search_tab)
        self.export_settings_grpbox.setGeometry(QtCore.QRect(370, 10, 351, 221))
        self.export_settings_grpbox.setStyleSheet("")
        self.export_settings_grpbox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.export_settings_grpbox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 30, 311, 75))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.export_checkbox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.export_checkbox.setChecked(True)
        self.export_checkbox.setObjectName("export_checkbox")
        self.export_checkbox.stateChanged.connect(self.export_csv_checkbox_function)
        self.verticalLayout_2.addWidget(self.export_checkbox)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_path_label = QtWidgets.QLabel(self.layoutWidget1)
        self.select_path_label.setObjectName("select_path_label")
        self.horizontalLayout_4.addWidget(self.select_path_label)
        spacerItem = QtWidgets.QSpacerItem(7, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.export_path_textedit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.export_path_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_path_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_path_textedit.setReadOnly(True)
        self.export_path_textedit.setObjectName("export_path_textedit")
        self.horizontalLayout_4.addWidget(self.export_path_textedit)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.path_select_toolbtn = QtWidgets.QToolButton(self.layoutWidget1)
        self.path_select_toolbtn.setObjectName("path_select_toolbtn")
        self.path_select_toolbtn.clicked.connect(self.open_directory_dialog)
        self.path_select_toolbtn.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 grey);\nborder-width: 5px;\nborder-radius: 10px;")
        self.horizontalLayout_7.addWidget(self.path_select_toolbtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.export_filename_label = QtWidgets.QLabel(self.layoutWidget1)
        self.export_filename_label.setObjectName("export_filename_label")
        self.horizontalLayout_3.addWidget(self.export_filename_label)
        self.export_filename_textedit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.export_filename_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.export_filename_textedit.setObjectName("export_filename_textedit")
        self.export_filename_textedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3.addWidget(self.export_filename_textedit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.proceed_btn_search = QtWidgets.QCommandLinkButton(self.new_search_tab)
        self.proceed_btn_search.clicked.connect(self.proceed_btn_search_function)
        self.proceed_btn_search.setGeometry(QtCore.QRect(620, 260, 101, 41))
        self.proceed_btn_search.setObjectName("proceed_btn_search")
        self.proceed_btn_search.setStyleSheet("")
        self.tabWidget.addTab(self.new_search_tab, "")
        self.import_tab = QtWidgets.QWidget()
        self.import_tab.setObjectName("import_tab")
        self.listWidget = ListView(self.import_tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 40, 731, 201))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setObjectName("listWidget")
        self.add_btn = QtWidgets.QPushButton(self.import_tab)
        self.add_btn.setGeometry(QtCore.QRect(650, 10, 31, 23))
        self.add_btn.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 grey);\nborder-width: 5px;\nborder-radius: 10px;\ncolor: green;")
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
        self.remove_btn.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 grey);\nborder-width: 5px;\nborder-radius: 10px;\ncolor: red;")
        self.remove_btn.setObjectName("remove_btn")
        self.remove_btn.setFont(font)
        self.remove_btn.setEnabled(False)
        self.proceed_btn_stats = QtWidgets.QCommandLinkButton(self.import_tab)
        self.proceed_btn_stats.setGeometry(QtCore.QRect(620, 260, 101, 41))
        self.proceed_btn_stats.setObjectName("proceed_btn_stats")
        self.proceed_btn_stats.setStyleSheet("")
        self.tabWidget.addTab(self.import_tab, "")
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
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.triggered.connect(self.logout)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionExit.setObjectName("actionLogout")
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.search_settings_grpbox.setTitle(_translate("MainWindow", "Search Settings"))
        self.uni_radio_btn.setText(_translate("MainWindow", "University Of Macedonia"))
        self.year_label.setText(_translate("MainWindow", "Year:"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.src_type_label.setText(_translate("MainWindow", "Source Type:"))
        self.src_type_combobox.setItemText(0, _translate("MainWindow", "Journals"))
        self.src_type_combobox.setItemText(1, _translate("MainWindow", "Conference Proceedings"))
        self.src_type_combobox.setItemText(2, _translate("MainWindow", "Book Series"))
        self.src_type_combobox.setItemText(3, _translate("MainWindow", "Books"))
        self.export_settings_grpbox.setTitle(_translate("MainWindow", "Export Settings"))
        self.export_checkbox.setText(_translate("MainWindow", "Export results to CSV"))
        self.select_path_label.setText(_translate("MainWindow", "Select Export Path:"))
        self.export_path_textedit.setPlaceholderText(_translate("MainWindow", "Export Path..."))
        self.path_select_toolbtn.setText(_translate("MainWindow", "..."))
        self.export_filename_label.setText(_translate("MainWindow", "Select CSV Filename:"))
        self.proceed_btn_search.setText(_translate("MainWindow", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.new_search_tab), _translate("MainWindow", "New Search"))
        self.proceed_btn_stats.setText(_translate("MainWindow", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.import_tab), _translate("MainWindow", "Import CSVs"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.remove_btn.setToolTip(_translate("MainWindow", "Remove CSV from list"))
        self.remove_btn.setText(_translate("MainWindow", "-"))
        self.add_btn.setToolTip(_translate("MainWindow", "Add CSV"))
        self.add_btn.setText(_translate("MainWindow", "+"))

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

        dialog = QtWidgets.QDialog()
        dialog.dialog_ui = Ui_ScanDialog()
        dialog.dialog_ui.setupUi(dialog, self.MainWindow, self.generate_query())
        dialog.exec_()

    def open_directory_dialog(self):

        '''
        When user hits the tool button,
        a dialog appears, in order the user to choose the folder
        in which the csv will be exported after the completion of search

        '''
        dir_ = QFileDialog.getExistingDirectory(self.MainWindow, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
        self.export_path_textedit.setText(dir_)

    def open_file_dialog(self):
        '''
        When user hits the add button,
        a dialog appears, in order the user to choose csv file
        When ok is clicked, file's path is added to list widget

        '''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filenames = QFileDialog.getOpenFileNames(None,"Open", "","Text Files (*.csv)", options=options)
        for filename in filenames[0]:
            self.listWidget.addItem(filename)

    def export_csv_checkbox_function(self):

        '''
        If user unchecks the "Export CSV", then
        he will not be able to choose path or filename (because there will be no file)

        '''

        if not self.export_checkbox.isChecked():
            self.path_select_toolbtn.setEnabled(False)
            self.export_filename_textedit.setEnabled(False)
            self.export_filename_textedit.setStyleSheet("background-color: rgb(190, 190, 190);")
        else:
            self.path_select_toolbtn.setEnabled(True)
            self.export_filename_textedit.setEnabled(True)
            self.export_filename_textedit.setStyleSheet("background-color: rgb(255, 255, 255);")

    def generate_query(self):

        '''
        This function generates a specific search query
        according to user's choices (from menu UI)
        Returns the query (str)

        '''
        
        pub_year = self.dateEdit.text()

        src_type = 'j' # by default

        if self.src_type_combobox.currentText() == 'Journals':
            src_type = 'j'
        elif self.src_type_combobox.currentText() == 'Books':
            src_type = 'b'
        elif self.src_type_combobox.currentText() == 'Book Series':
            src_type = 'k'
        elif self.src_type_combobox.currentText() == 'Conference Proceedings':
            src_type = 'p'

        query = '( AF-ID ( "Panepistimion Makedonias"   60001086 ) )  AND  ( LIMIT-TO ( PUBYEAR ,  '+pub_year+' ) )  AND  ( LIMIT-TO ( SRCTYPE ,  "'+src_type+'" ) )'

        return query

    def logout(self):

        '''
        This function brings user to login window
        in order to login again with the same or
        different scopus account
        Triggered on Logout click (menu bar) or on CTRL+L pressed

        '''
        browser.get(login_url)
        self.login_ui = login_gui_backend.Ui_MainWindow()
        self.login_ui.setupUi(self.MainWindow)
        self.MainWindow.show()
  
class Ui_ScanDialog(object):
    def setupUi(self, ScanDialog, MainWindow, query):
        self.MainWindow = MainWindow
        self.ScanDialog = ScanDialog
        self.ScanDialog.setObjectName("ScanDialog")
        self.ScanDialog.resize(440, 108)
        self.ScanDialog.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 darkslategray, stop:1 grey);")
        self.buttonBox = QtWidgets.QDialogButtonBox(ScanDialog)
        self.buttonBox.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 grey);\nborder-width: 5px;\nborder-radius: 10px;\ncolor: red;")
        self.buttonBox.setGeometry(QtCore.QRect(10, 70, 421, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setEnabled(False)
        self.progressBar = QtWidgets.QProgressBar(ScanDialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 421, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(ScanDialog)
        self.buttonBox.accepted.connect(ScanDialog.accept)
        self.buttonBox.rejected.connect(self.cancel_analysis)
        QtCore.QMetaObject.connectSlotsByName(ScanDialog)

        self.query = query
        self.start_search()

    def start_search(self):

        '''
        This function starts a new thread,
        in order the search to begin (using the generated query)
        After search is done, document analysis begins

        '''
        if browser.current_url != search_url:
            browser.get(search_url)

        self.search_thread = SearchThread(parent=None, query=self.query)
        self.search_thread.finished.connect(self.start_doc_analysis)
        self.search_thread.start()
            

    def start_doc_analysis(self):

        '''
        This function starts a new thread,
        in order the analysis of the documents to begin

        '''
        self.analysis_thread = AnalysisThread(parent=None)
        self.analysis_thread.total_docs_update.connect(self.set_progress_bar_max_value)
        self.analysis_thread.update_progress_bar.connect(self.update_progress_bar_value)
        self.analysis_thread.thread_finished.connect(self.open_question_box)
        self.analysis_thread.start()

    def open_question_box(self, results):

        '''
        This function opens a question box
        in order to ask the user whether
        he wants to open the results window or not
        Triggered when analysis operation is finished

        '''

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setText('Analysis finished! Show results?')
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        msg.setWindowTitle("Success")
        reply = msg.exec_()

        if reply == QtWidgets.QMessageBox.Yes:
            
            self.ScanDialog.close()
            self.MainWindow.close()
            self.ResultsWindow = QtWidgets.QMainWindow()
            self.results_ui = results_gui_backend.Ui_ResultsWindow()
            self.results_ui.setupUi(self.ResultsWindow, results)
            self.ResultsWindow.show()

        elif reply == QtWidgets.QMessageBox.No:
            self.ScanDialog.close()

    def cancel_analysis(self):

        '''
        This function closes scan dialog
        and ends search and analysis operation
        Triggered on cancel click

        '''
        self.ScanDialog.close()
        
        try:
            self.search_thread.stop()
        except:
            print('No search thread found')

        try:
            self.analysis_thread.stop()  
        except:
            print('No analysis thread found')
        
    def update_progress_bar_value(self, value):

        '''
        This function updates the progress bar
        according to the number of read documents

        '''
        self.progressBar.setValue(value)

    def set_progress_bar_max_value(self, max_value):
        '''
        This function is used once, in the beginning of analysis
        Sets the maximum value of progress bar

        '''
        self.progressBar.setMaximum(max_value)

    def retranslateUi(self, ScanDialog):
        _translate = QtCore.QCoreApplication.translate
        ScanDialog.setWindowTitle(_translate("ScanDialog", "Scanning..."))
        self.progressBar.setFormat(_translate("ScanDialog", "%p%"))

class SearchPage():

    def __init__(self):
        self.advanced_ref_link_text = 'Advanced'
        self.search_field_id = 'searchfield'
        self.search_btn_id = 'advSearch'

    def search(self, query):
        '''
        Searches for sources, with given query
        in Scopus

        '''

        advanced_ref = WebDriverWait(browser, DELAY_TIME).until(    # when page is loaded, click Advanced Search
            EC.presence_of_element_located((By.LINK_TEXT, self.advanced_ref_link_text)))
        advanced_ref.click()

        search_field = WebDriverWait(browser, DELAY_TIME).until(    # when page is loaded, click query text box & send our query
            EC.presence_of_element_located((By.ID, self.search_field_id)))
        search_field.clear()
        search_field.send_keys(query)

        search_btn = browser.find_element_by_id(self.search_btn_id)    # when query is sent, find & press the search button
        search_btn.click()

class SearchThread(QtCore.QThread):

    '''
    Search thread
    Performs the document search in separated thread
    Query is generated according to user's selections (menu UI)

    '''
    def __init__(self, parent=None, query=''):
        super(SearchThread, self).__init__(parent)
        self.query = query

    # run method gets called when we start the thread
    def run(self):
        search_page = SearchPage()
        search_page.search(self.query)

    def stop(self):
        self.terminate()

class DocumentPage():

    def __init__(self, thread, total_docs_signal, update_progress_bar_signal):
        self.percentile_categories_class_name = 'treeLineContainer'
        self.percentiles_xpath = '//*[contains(@class, "pull-left paddingLeftQuarter")]'
        self.metric_values_xpath = "//*[contains(@class, 'value fontMedLarge lineHeight2 blockDisplay')]"
        self.paging_ul_class_name = 'pagination'
        self.doc_source_class_name = 'ddmDocSource'      
        self.search_results_table_id = 'srchResultsList'
        self.doc_title_class_name = 'ddmDocTitle'
        self.authors_list_class_name = 'ddmAuthorList'
        self.pub_year_class_name = 'ddmPubYr'
        self.docs_total_number = 'resultsCount'

        self.total_docs_update = total_docs_signal
        self.update_progress_bar = update_progress_bar_signal

        self.analysis_thread = thread

    def analyze_documents(self):

        '''
        Scans every source & gets its rating
        Saves all percentiles, average of percentiles and name of source
        in a dictionary, which is appended in a list of dictionaries (all sources)

        '''
        final_lst = []
        curr_page = 1   # begin with page 1
        no_of_pages = self.get_number_of_pages() # get total number of pages
        document_rows = self.get_document_rows() # get all document names
        author_rows = self.get_author_rows() # get all author names
        source_rows = self.get_source_rows()    # get all source names
        year_rows = self.get_year_rows() # get all years
        total_docs = self.get_total_number_of_docs()    # get the number of total docs
        self.total_docs_update.emit(total_docs)
        i=1
        while True:

            try:
                document_name = document_rows.popleft() # pop the first one in list
                author_list = author_rows.popleft()
                source_name = source_rows.popleft()
                year = year_rows.popleft()

                if source_name['clickable']:
                    source = WebDriverWait(browser, DELAY_TIME).until(    
                        EC.presence_of_element_located((By.LINK_TEXT, source_name['name'])))   # go in document's page
                    source.click()

                    try:
                        categories = WebDriverWait(browser, DELAY_TIME).until(    
                            EC.presence_of_all_elements_located((By.CLASS_NAME, self.percentile_categories_class_name)))    # find categories names

                        categories = self.convert_to_txt(categories) # convert categories from web element to string

                        try:
                            percentiles = WebDriverWait(browser, DELAY_TIME).until(    
                                EC.presence_of_all_elements_located((By.XPATH, self.percentiles_xpath))) # find percentiles

                            percentiles = self.percentiles_to_num(self.convert_to_txt(percentiles))   # convert percentiles to number (int)

                            print(percentiles)

                        except:
                            print('no percentiles found')

                        try:

                            # metric_values = WebDriverWait(browser, DELAY_TIME).until(    
                            #     EC.presence_of_all_elements_located((By.XPATH, self.metric_values_xpath))) # find metrics (num)

                            # metric_values = self.convert_to_txt(metric_values)

                            try:
                                citescore_element = WebDriverWait(browser, DELAY_TIME).until(    
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="rpCard"]/h2/span')))

                                citescore = citescore_element.text
                            except:
                                citescore = 0

                            try:
                                sjr_element = WebDriverWait(browser, DELAY_TIME).until(    
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="sjrCard"]/h2/span')))
                                
                                sjr = sjr_element.text
                            except:
                                sjr = 0

                            try:
                                snip_element = WebDriverWait(browser, DELAY_TIME).until(    
                                    EC.presence_of_element_located((By.XPATH, '//*[@id="snipCard"]/h2/span')))

                                snip = snip_element.text
                            except:
                                snip = 0

                            metric_values = [citescore, sjr, snip]
                        
                        except:
                            print('no metric values found')

                        document_dict = self.create_dict(i, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), self.get_average_percentile(percentiles), zip(['CiteScore', 'SJR', 'SNIP'], metric_values))

                        final_lst.append(document_dict)

                        print(document_dict)

                        self.update_progress_bar.emit(i)

                        i+=1

                        browser.execute_script("window.history.go(-1)") # go to the previous page
                    except:
                        document_dict = self.create_dict(i, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), 0, zip(['CiteScore', 'SJR', 'SNIP'], [0, 0, 0]))
                        final_lst.append(document_dict)
                        self.update_progress_bar.emit(i)
                        i+=1
                        print(document_dict)
                        browser.execute_script("window.history.go(-1)") # go to the previous page
                else:
                    document_dict = self.create_dict(i, document_name, source_name['name'], year, author_list, self.get_number_of_authors(author_list), 0, zip(['CiteScore', 'SJR', 'SNIP'], [0, 0, 0]))
                    final_lst.append(document_dict)
                    self.update_progress_bar.emit(i)
                    i+=1
                    print(document_dict)
            except:
                try:
                    if curr_page < no_of_pages:
                        curr_page = self.change_page(curr_page)  # change page
                        document_rows = self.get_document_rows() # get all document names
                        author_rows = self.get_author_rows() # get all author names
                        source_rows = self.get_source_rows()    # get all source names
                        year_rows = self.get_year_rows() # get all years
                    else:
                        break
                except:
                    break

        return final_lst

    def remove_digits(self, lst): 
        '''
        Takes a list of strings and
        removes digits from every element
        '''
        pattern = '[0-9]'
        lst = [re.sub(pattern, '', i) for i in lst]
        return lst

    def remove_spaces(self, lst):
        '''
        Takes a list of strings and
        removes spaces from every element
        '''
        lst = [x.strip(' ') for x in lst]
        return lst

    def remove_new_line(self, lst):
        '''
        Takes a list of strings and
        removes spaces from every element
        '''
        lst = [x.strip('\n.') for x in lst]
        return lst

    def create_dict(self, i, doc_name, source_name, year, authors, num_of_authors, avg_percentile, metrics):
        '''
        Takes some lists & a dictionary with info
        and creates a dictionary for each document with
        all the info needed
        '''
        dictionary = {'#': i, 'Document Name': doc_name, 'Source Name': source_name, 'Year': year, 'Authors': authors, '# Authors': num_of_authors, 'Average Percentile': avg_percentile}
        dictionary.update(metrics)
        return dictionary

    def get_number_of_authors(self, authors):
        '''
        Takes a string (author names) & returns
        an integer (total number of document's authors)
        '''
        split_authors = authors.split(',')
        return len([','.join(i) for i in zip(split_authors[::2], split_authors[1::2])])

    def convert_to_txt(self, lst):
        '''
        Takes a list of web elements & returns
        a list of strings (the string of each element)
        '''
        return [element.text for element in lst]

    def percentiles_to_num(self, lst):
        '''
        Takes a list of strings and takes the numbers
        from each element (percentiles). Returns a list of nums.
        '''
        percentiles_num = []
        for percentile in lst:
            percentiles_num.append(int(re.findall("\d+", percentile)[0]))
        return percentiles_num

    def get_average_percentile(self, percentiles):
        '''
        Takes a list of numbers (percentiles) 
        and returns their average
        '''
        average = float(sum(percentiles) / len(percentiles))
        return round(average, 2)

    def change_page(self, curr_page):
        '''
        Takes a number of page (int) and finds the next page
        If a next page is found, goes to next page
        If not, script exits (no other pages left)
        Returns the new curr_page
        '''
        try:
            paging_ul = WebDriverWait(browser, DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                EC.presence_of_element_located((By.CLASS_NAME, self.paging_ul_class_name)))
            pages = paging_ul.find_elements_by_tag_name('li')

            next_page = next(page for page in pages if page.text == str(curr_page+1))

            next_page.click()

            return curr_page+1

        except:
            print('error')

    def get_number_of_pages(self):
        '''
        Returns total number of pages
        '''
        paging_ul = WebDriverWait(browser, DELAY_TIME).until(    # when page is loaded, click query text box & send our query
                EC.presence_of_element_located((By.CLASS_NAME, self.paging_ul_class_name)))
        return len(paging_ul.find_elements_by_tag_name("li"))

    def get_number_of_rows(self):
        '''
        Returns the number of rows
        of a page (number of documents)
        '''
        elements = []
        i=0
        while True:
            try:
                elements.append(browser.find_element_by_xpath('//*[@id="resultDataRow'+str(i)+'"]'))
                i+=1
            except:
                break
        return len(elements)

    def get_total_number_of_docs(self):
        '''
        Returns the total number of documents (that will be scanned)
        Used for scan dialog's progress bar
        '''
        total_docs_num = browser.find_element(By.CLASS_NAME, self.docs_total_number)
        return int(total_docs_num.text)

    def get_source_rows(self):
        '''
        Fetches all sources (names)
        and returns a string queue (with all the names)
        '''
        rows = []

        no_of_rows = self.get_number_of_rows()    # number of rows of current page

        i=1
        while i<=no_of_rows:
            td = WebDriverWait(browser, DELAY_TIME).until(    
                EC.presence_of_element_located((By.XPATH, '//*[@id="resultDataRow'+str(i-1)+'"]/td[4]'))) 
            try:
                row = td.find_element(By.CLASS_NAME, self.doc_source_class_name)
                rows.append({'name': row.text, 'clickable': True})
                i+=1
            except:
                rows.append({'name': td.text.splitlines()[0], 'clickable': False})
                i+=1

        return deque(rows)

    def get_document_rows(self):
        '''
        Fetches all documents (names)
        and returns a string queue (with all the names)
        '''
        results = WebDriverWait(browser, DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.doc_title_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

    def get_author_rows(self):
        '''
        Fetches all authors (names)
        and returns a string queue (with all the names)
        '''
        results = WebDriverWait(browser, DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.authors_list_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

    def get_year_rows(self):
        '''
        Fetches all years
        and returns a string queue (with all the years)
        '''
        results = WebDriverWait(browser, DELAY_TIME).until(    
            EC.presence_of_element_located((By.ID, self.search_results_table_id))) # srchResultsList is the data table, from which we will get the documents' names
        rows = results.find_elements(By.CLASS_NAME, self.pub_year_class_name) # get all of the rows in the table
        rows = self.convert_to_txt(rows) # convert web elements to string
        return deque(rows)

class AnalysisThread(QtCore.QThread):

    '''
    Analysis thread
    Performs the document analysis in separated thread

    '''

    total_docs_update = QtCore.pyqtSignal(int)
    update_progress_bar = QtCore.pyqtSignal(int)

    thread_finished = QtCore.pyqtSignal(list)
    
    def __init__(self, parent=None):
        super(AnalysisThread, self).__init__(parent)

    # run method gets called when we start the thread
    def run(self):
        doc_page = DocumentPage(self, self.total_docs_update, self.update_progress_bar)
        results = doc_page.analyze_documents()

        self.thread_finished.emit(results)

    def stop(self):
        self.terminate()

if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
