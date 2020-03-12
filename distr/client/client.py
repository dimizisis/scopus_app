import socketio

sio = socketio.Client()

response_lst = None
progress = 0

class DesktopClientNamespace(socketio.ClientNamespace):

    HOST = 'http://localhost:5000'

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
        sio.emit(event='stop')
        print('disconnected from server')
        
    def connect_to_server(self):
        sio.connect(self.HOST)
        return True

    def update_process(self):
        response = sio.call(event='update')
        return response

    def get_response_lst(self):
        response = sio.call(event='get_final_lst')
        return response

    def stop_operation(self):
        sio.emit(event='stop')
        sio.disconnect()

    def make_search_request(self, query):
        response = sio.call(event='search', data=query)
        return response

    def start_analyzing(self):
        print('emitted analyze event')
        sio.emit(event='analyze')

    def get_total_docs(self):
        response = sio.call(event='get_total_docs')
        return response

    def disconnect(self):
        sio.disconnect()
        print('disconnected from server')

sio.register_namespace(DesktopClientNamespace('/desktop_client'))
