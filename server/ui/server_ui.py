
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append('../')
import eventlet
eventlet.monkey_patch()
import socketio
from analyze import DocumentPage
from search import SearchPage
import init
from threading import Lock

sio = socketio.Server()
app = socketio.WSGIApp(sio)

mutex = Lock()

search_page = None
doc_page = None

final_lst = list()
browser = init.init_browser()

@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def search(sid, data):
    global search_page
    mutex.acquire()
    search_page = SearchPage()
    response = search_page.search(data, sio, browser)
    mutex.release()
    return response

@sio.event
def get_total_docs(sid):
    global doc_page
    mutex.acquire()
    doc_page = DocumentPage()
    response = doc_page.get_total_number_of_docs(browser)
    mutex.release()
    return response

@sio.event
def analyze(sid):
    global doc_page
    mutex.acquire()
    doc_page.analyze_documents(sio, browser, final_lst)
    mutex.release()

@sio.event
def get_final_lst(sid):
    global final_lst
    final_lst = sorted(final_lst, key = lambda i: i['Average Percentile'], reverse=True)
    final_lst = add_id(final_lst)
    return final_lst

def add_id(lst):
    i=1
    for d in lst:
        d.update({"#": i})
        i += 1
    return lst

@sio.event
def update(sid):
    global final_lst
    return len(final_lst)

@sio.event
def disconnect(sid):
    global doc_page
    print('disconnect ', sid)
    try:
        doc_page.stop_analysis()
    except:
        pass
    finally:
        reset()

def reset():
    global doc_page, search_page, final_lst, browser
    mutex.acquire()
    final_lst = list()
    browser = init.reset_browser(browser)
    mutex.release()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 212)
        MainWindow.setMaximumSize(QtCore.QSize(433, 212))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logging_textedit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.logging_textedit.setReadOnly(True)
        self.logging_textedit.setObjectName("logging_textedit")
        self.verticalLayout.addWidget(self.logging_textedit)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.disconnect_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.disconnect_btn.setEnabled(False)
        self.disconnect_btn.setObjectName("disconnect_btn")
        self.gridLayout.addWidget(self.disconnect_btn, 0, 0, 1, 1)
        self.connect_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.connect_btn.setObjectName("connect_btn")
        self.gridLayout.addWidget(self.connect_btn, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.disconnect_btn.setText(_translate("MainWindow", "Disconnect"))
        self.connect_btn.setText(_translate("MainWindow", "Connect"))

    def connect(self):
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

    def disconnect(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
