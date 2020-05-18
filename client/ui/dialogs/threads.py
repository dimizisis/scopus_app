
from PyQt5 import QtCore
import sys
sys.path.append('../../')
from export.statistics import StatisticsExportation

class SearchThread(QtCore.QThread):
    '''
    Search thread
    Performs the document search in separated thread
    Query is generated according to user's selections (menu UI)
    '''
    stop_operation = False
    def __init__(self, parent=None, query='', client=None):
        super(SearchThread, self).__init__(parent)
        self.query = query
        self.client = client
        self.response = None

    # run method gets called when we start the thread
    def run(self):
        try:
            self.response = self.client.make_search_request(self.query)
            print(self.response)
        except:
            return

class AnalysisThread(QtCore.QThread):
    '''
    Analysis thread
    Performs the document analysis in separated thread
    '''
    total_docs_update = QtCore.pyqtSignal(int)
    update_progress_bar = QtCore.pyqtSignal(int)

    thread_finished = QtCore.pyqtSignal(list)
    
    def __init__(self, parent=None, excel_path=None, client=None, progressBar=None):
        super(AnalysisThread, self).__init__(parent)
        self.excel_path = excel_path
        self.client = client
        self.progressBar = progressBar
        self.stop = False

    # run method gets called when we start the thread
    def run(self):
        total_docs = self.client.get_total_docs()
        self.total_docs_update.emit(total_docs)
        self.client.start_analyzing()

        import time

        while True:
            if self.stop:
                return
            try:
                response = self.client.update_process()
                self.progressBar.setValue(response)
                if total_docs == response:
                    results_lst = self.client.get_response_lst()
                    self.client.disconnect()
                    print(f't.d: {total_docs}, response: {response}')
                    break
                time.sleep(5)
            except:
                return
                
        print(results_lst)
        self.thread_finished.emit([results_lst, self.excel_path])

    def stop_analysis(self):
        self.stop = True
