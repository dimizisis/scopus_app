import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def search_response(data):
    if data == 'ok':
        print(data)
        sio.emit(event='analyze')

@sio.event
def analyze_response(data):
    print(data)

@sio.event
def total_docs(data):
    print(data)

@sio.event
def update_process(data):
    print(data)

@sio.event
def disconnect():
    sio.emit(event='stop')
    print('disconnected from server')

sio.connect('http://localhost:5000')
sio.emit(event='search', data='( AF-ID ( "Panepistimion Makedonias"   60001086 ) )  AND  ( LIMIT-TO ( PUBYEAR ,  2018 ) )  AND  ( LIMIT-TO ( SRCTYPE ,  "j" ) )')
try:
    sio.wait()
except Exception:
    sio.disconnect()