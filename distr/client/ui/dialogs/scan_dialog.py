
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import sys
sys.path.append('../')
from helper_functions.export import write_to_excel
from client import DesktopClientNamespace, progress, response_lst

class Ui_ScanDialog(object):
    def setupUi(self, ScanDialog, MainWindow, query, excel_export, excel_path):

        import os
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.client = DesktopClientNamespace()
        success = self.client.connect_to_server()

        if not success[0]:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowIcon(QIcon(scriptDir + os.path.sep + '..\\style\\images\\favicon.ico'))
            msg.setText(success[1])
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
            msg.setWindowTitle('Failed to connect')
            reply = msg.exec_()
            return False
        else:
            import dialogs.threads as threads
            self.search_thread = threads.SearchThread(query=self.query, client=self.client)
            self.analysis_thread = threads.AnalysisThread(excel_path=self.excel_path, client=self.client, progressBar=self.progressBar)
            self.start_search()

        self.MainWindow = MainWindow
        self.ScanDialog = ScanDialog
        self.ScanDialog.setObjectName("ScanDialog")
        self.ScanDialog.resize(440, 108)
        self.ScanDialog.setMaximumSize(QtCore.QSize(440, 108))
        self.ScanDialog.setMinimumSize(QtCore.QSize(440, 108))
        self.excel_export = excel_export
        self.excel_path = excel_path
        self.buttonBox = QtWidgets.QDialogButtonBox(ScanDialog)
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
        self.ScanDialog.setWindowIcon(QIcon(scriptDir + os.path.sep + '..\\style\\images\\favicon.ico')) 

        self.retranslateUi(ScanDialog)
        self.buttonBox.accepted.connect(ScanDialog.accept)
        self.buttonBox.rejected.connect(self.cancel_analysis)
        QtCore.QMetaObject.connectSlotsByName(ScanDialog)

        self.query = query

        return True

    def start_search(self):
        '''
        This function starts a new thread,
        in order the search to begin (using the generated query)
        After search is done, document analysis begins
        ''' 
        self.search_thread.finished.connect(self.start_doc_analysis)
        self.search_thread.start()

    def start_doc_analysis(self):
        '''
        This function starts a new thread,
        in order the analysis of the documents to begin
        '''
        if not self.search_thread.stop_operation and self.search_thread.response == 'ok':
            print('search response: ' +self.search_thread.response)  
            self.analysis_thread.total_docs_update.connect(self.set_progress_bar_max_value)
            self.analysis_thread.update_progress_bar.connect(self.update_progress_bar_value)
            if self.excel_export:
                self.analysis_thread.thread_finished.connect(write_to_excel)
            self.analysis_thread.thread_finished.connect(self.open_question_box)
            self.analysis_thread.start()

    def open_question_box(self, results_lst):
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

            import results_ui
            
            self.ScanDialog.close()
            self.MainWindow.close()
            self.ResultsWindow = QtWidgets.QMainWindow()
            self.results_ui = results_ui.Ui_ResultsWindow()
            self.results_ui.setupUi(self.ResultsWindow, results_lst)
            self.ResultsWindow.show()

        elif reply == QtWidgets.QMessageBox.No:
            self.ScanDialog.close()

    def cancel_analysis(self):
        '''
        This function closes scan dialog
        and ends search and analysis operation
        Triggered on cancel click
        '''
        self.buttonBox.setEnabled(False)
        self.progressBar.setEnabled(False)

        try:
            self.client.disconnect()
        except:
            print('No client found')

        try:
            self.analysis_thread.stop_analysis()
            print('analysis stopped')
        except:
            print('No analysis thread found')

        self.ScanDialog.close()
        
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