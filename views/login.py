#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286

import tkinter as tk
from tkinter import ttk

class LogInView(ttk.Frame):
    def __init__(self):
        super().__init__()
        options = {'padx': 2, 'pady': 2}
        ttk.Style().configure("MainFrame.TFrame", background='#283359')
        self.config(style="MainFrame.TFrame")


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.middleframe1 = ttk.Frame(self)
        self.middleframe1.config(style="MainFrame.TFrame")
        self.middleframe1.grid(column=1, row=1, sticky="nsew")

        self.leftframe = ttk.Frame(self.middleframe1)
        self.leftframe.config(style="MainFrame.TFrame")
        self.leftframe.pack(side="left", expand=True, fill="both")
        self.rightframe = ttk.Frame(self.middleframe1)
        self.rightframe.config(style="MainFrame.TFrame")
        self.rightframe.pack(side="right", expand=True, fill="both")


        self.username_label = ttk.Label(self.leftframe, text="StaffID: ", background="#283359", foreground="white", font=("Arial", 40))
        self.username_input = ttk.Entry(self.rightframe, width=8, background="white", font=("Arial", 40))
        self.username_label.pack(side="top")
        self.username_input.pack(side="top")

        self.password_label = ttk.Label(self.leftframe, text="Password: ", background="#283359", foreground="white", font=("Arial", 40))
        self.password_input = ttk.Entry(self.rightframe, width=8, show="*", background="#283359", font=("Arial", 40))
        self.password_label.pack(side="top", pady=10)
        self.password_input.pack(side="top", pady=10)

        self.restaurant_label = ttk.Label(self.leftframe, text="Restaurant ID: ", background="#283359", foreground="white", font=("Arial", 40))
        self.restaurant_input = ttk.Entry(self.rightframe, width=8, background="#283359", font=("Arial", 40))
        self.restaurant_label.pack(side="top", pady=10)
        self.restaurant_input.pack(side="top", pady=10)


        self.login_btn = tk.Button(self, text="Sign In", font=("Arial", 40), height=1, width=8)
        self.login_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)