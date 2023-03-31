import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created (sefl,event):
        print(f'hi{event.src_path}it has been created')
        
    #2_on_deleted
    def on_deleted (sefl,event):
        print(f'oops something is deleted {event.src_path}')

    def on_modified (sefl,event):
        print(f'{event.src_path} it is modified')
    #4_on_moved
    def on_moved (sefl,event):
        print(f'{event.src_path} it is moved')
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
 while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
 print('stopped!')
 observer.stope()






