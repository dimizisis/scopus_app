
import eventlet
eventlet.monkey_patch()
import socketio
from analyze import DocumentPage
from search import SearchPage
import init
from threading import Lock
import configparser
import os

sio = socketio.Server()
app = socketio.WSGIApp(sio)

mutex = Lock()

search_page = None
doc_page = None

final_lst = list()
browser = init.init_browser()

def import_settings():
    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(os.path.realpath(__file__))+'/settings.ini')

    ip = parser.get('SYSTEM_SETTINGS', 'IP')
    port = int(parser.get('SYSTEM_SETTINGS', 'PORT'))

    return ip, port

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
    browser.delete_all_cookies()
    browser.get(init.search_url)
    mutex.release()
        
if __name__ == '__main__':
    ip, port = import_settings()
    eventlet.wsgi.server(eventlet.listen((ip, port)), app)
