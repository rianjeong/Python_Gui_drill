from tkinter import *
import tkinter as tk
from tkinter import filedialog
import time
import shutil
import os
import Gui_drill_main
import Gui_drill_Gui
from datetime import timedelta, datetime


source_file = []
destination_file = []
sourceText = "Select Source"
destinationText = "Select Destination"
executeText = "Files Transfered"
nothing = "No Files Found"


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "okay to exit application?"):
        #this closes app
        self.master.destroy()
        os._exit(0)

#defining functions for destination, source and execute

def destinationDir(self):
    destName = filedialog.askdirectory()
    self.Dest_button["text"] = str(destName) if destName else destinationText
    destination = destName + "/"
    destination_file.append(destination)
    print(destination)
    

def executeDir(self):
    findFile(self)
    self.Ex_button["text"] = str(executeText) if executeDir else executeText


def findFile(self):
    source = source_file[0]
    destination = destination_file[0]
    now = time.time()
    diff_sec = float(24*3600)
    before = now - diff_sec


    for files in os.listdir(source):
        src_file = os.path.join(source, files)
        dst_file = os.path.join(destination, files)
        st = os.stat(src_file)

        mod_time = datetime.fromtimestamp(st.st_mtime)
        new_time = time.mktime(mod_time.timetuple())
    if new_time > before:
        shutil.copy(src_file, dst_file)
        print("files have been transfered")
    else:
        print("Not a new file")

def sourceDir(self):
    sourceName = filedialog.askdirectory()
    self.Src_button["text"] = str(sourceName) if sourceName else sourceText
    source = sourceName + "/"
    source_file.append(source)
    print(source)

    conn.close()

if __name__ == "__main__":
    pass





