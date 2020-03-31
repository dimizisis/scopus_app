
import socketio
import configparser
import os
import sys
sys.path.append('../')

sio = socketio.Client()

response_lst = None
progress = 0

def import_settings():
    parser = configparser.ConfigParser()
    parser.read(os.path.dirname(os.path.realpath(__file__))+'\\settings.ini')

    events = dict()
    namespace = parser.get('SYSTEM_SETTINGS', 'CLIENT_NAMESPACE')
    host = parser.get('SYSTEM_SETTINGS', 'HOST')
    events.update({'stop_event': parser.get('SYSTEM_SETTINGS', 'STOP_EVENT')})
    events.update({'update_event': parser.get('SYSTEM_SETTINGS', 'UPDATE_EVENT')})
    events.update({'get_lst_event': parser.get('SYSTEM_SETTINGS', 'GET_LIST_EVENT')})
    events.update({'search_event': parser.get('SYSTEM_SETTINGS', 'SEARCH_EVENT')})
    events.update({'get_total_docs_event': parser.get('SYSTEM_SETTINGS', 'GET_TOTAL_DOCS_EVENT')})

    return namespace, host, events

class DesktopClientNamespace(socketio.ClientNamespace):

    NAMESPACE, HOST, EVENTS = import_settings()

    print(HOST)

    def __init__(self, namespace=None):
        super().__init__(namespace=namespace)

    @sio.event
    def on_connect(self):
        print('connection established')

    @sio.event
    def on_analyze_response(self, data):
        global response_lst
        response_lst = data
        print(response_lst)

    @sio.event
    def on_update_process(self, data):
        global progress
        progress = data

    @sio.event
    def on_disconnect(self):
        sio.emit(event=self.EVENTS['stop_event'])
        print('disconnected from server')
        
    def connect_to_server(self):
        sio.connect(self.HOST)
        return True

    def update_process(self):
        response = sio.call(event=self.EVENTS['update_event'])
        return response

    def get_response_lst(self):
        response = sio.call(event=self.EVENTS['get_lst_event'])
        return response

    def stop_operation(self):
        sio.emit(event=self.EVENTS['stop_event'])
        sio.disconnect()

    def make_search_request(self, query):
        response = sio.call(event=self.EVENTS['search_event'], data=query)
        return response

    def start_analyzing(self):
        print('emitted analyze event')
        sio.emit(event='analyze')

    def get_total_docs(self):
        response = sio.call(event=self.EVENTS['get_total_docs_event'])
        return response

    def disconnect(self):
        sio.disconnect()
        print('disconnected from server')

sio.register_namespace(DesktopClientNamespace('/desktop_client'))
