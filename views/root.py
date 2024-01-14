#Zak Kannemeyer 22021286

import tkinter as tk

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        start_width = 1024
        min_width = 1024
        start_height = 768
        min_height = 768

        self.geometry(f"{screen_width-100}x{screen_height-100}")
        self.minsize(width=min_width, height=min_height)
        self.state('zoomed')
        #self.attributes('-fullscreen', True)
        #self.resizable(width="False", height="False")
        self.title("Horizon Restaurant Management System")
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)