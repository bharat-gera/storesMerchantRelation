import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import requests

file_path = '/home/bharat/file/'

class MyHandler(PatternMatchingEventHandler):
    patterns = ['*.json']
    
    def process(self, event):
        payload = {'data':event.src_path}
        return requests.get('http://127.0.0.1:8000/store/info/',params=payload)
    
    def on_created(self, event):
        self.process(event)



if __name__ == '__main__':
    observer = Observer()
    observer.schedule(MyHandler(), path=file_path)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()