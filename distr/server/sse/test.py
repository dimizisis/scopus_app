import eventlet
eventlet.monkey_patch()

class Analyzer:
    def __init__(self):
        self.stop_loop = False
    def analyze_documents(self, sio):
        while True:
            if self.stop_loop == True: break
            message = 'Let us go'
            sio.emit(event='response', data=message)
            print('let us go')
            eventlet.sleep(3)
    def stop(self):
        print('stop!')
        self.stop_loop = True
