import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/hp/Desktop/python/project 103"

class FileEventHandler(FileSystemEventHandler) :

    def on_created(self, event) :
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
