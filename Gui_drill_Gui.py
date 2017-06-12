from tkinter import *
import tkinter as tk
import Gui_drill_main
import Gui_drill_func



def load_gui(self):
    self.Src_button = tk.Button(self.master, text = "Find Source", command = lambda: Gui_drill_func.sourceDir(self))
    self.Src_button.grid(row = 1, column = 1, sticky = N+E+S+W)
    self.Dest_button = tk.Button(self.master, text = "Find Destination", command = lambda: Gui_drill_func.destinationDir(self))
    self.Dest_button.grid(row = 2, column = 1, sticky =  N+E+S+W)
    self.Ex_button = tk.Button(self.master, text = "Execute", command = lambda: Gui_drill_func.executeDir(self))
    self.Ex_button.grid(row = 3, column = 1, sticky = N+S+E+W)

    self.Src_label = tk.Label(self.master, text = "Source File:",)
    self.Src_label.grid(row = 1, column = 0, sticky = W)
    self.Src_label = tk.Label(self.master, text = "Destination File:")
    self.Src_label.grid(row = 2, column = 0, sticky = W)
    self.Ex_label = tk.Label(self.master, text = "Execute File Move:")
    self.Ex_label.grid(row = 3, column = 0, sticky = W)


if __name__ == "__main__":
    pass
