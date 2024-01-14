#Phoenix Burke Chang 21026891

import tkinter as tk
from tkinter import ttk


class ManagerFunctionsView(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.config(style="MainFrame.TFrame")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        self.rowconfigure(2, weight=1)
        
        self.f1 = ttk.Frame(self)
        self.f1.columnconfigure(0, weight=1, uniform='a')
        self.f1.columnconfigure(1, weight=1, uniform='a')
        self.f1.columnconfigure(2, weight=2, uniform='a')
        self.f1.columnconfigure(3, weight=1, uniform='a')
        self.f1.columnconfigure(4, weight=1, uniform='a')
        self.f1.rowconfigure(0, weight=1)
        self.f1.grid(row=0, sticky="nwes")

        self.back_btn = tk.Button(self.f1, text="Back", font=("Arial", 15))
        self.back_btn.grid(column=0, row=0, rowspan=2, columnspan=1, sticky="nsew")

        self.header = ttk.Label(self.f1, text="Manager Functions", font=("Arial", 30), anchor="center")
        self.header.grid(column=2, row=1, sticky="nsew", columnspan=1)

        self.staffname_label = ttk.Label(self.f1, text="Operator: placeholder", font=("Arial", 10), anchor="center")
        self.staffname_label.grid(column=4, row=0, sticky="sw")

        self.staffid_label = ttk.Label(self.f1, text="ID: placeholder", font=("Arial", 10), anchor="center")
        self.staffid_label.grid(column=4, row=1, sticky="nw")


        self.f2 = ttk.Frame(self)
        f2options = {'padx': 15, 'pady': 15}
        self.f2.config(style="MainFrame.TFrame")
        self.f2.columnconfigure(0, weight=1, uniform='a')
        self.f2.columnconfigure(1, weight=1, uniform='b')
        self.f2.columnconfigure(2, weight=1, uniform='b')
        self.f2.columnconfigure(3, weight=1, uniform='b')
        self.f2.columnconfigure(4, weight=1, uniform='a')
        self.f2.rowconfigure(0, weight=1, uniform='c')
        self.f2.rowconfigure(1, weight=1, uniform='c')
        self.f2.grid(row=1, sticky="nsew", pady=(10, 0))

        self.crud_menu_btn = tk.Button(self.f2, text="CRUD Menu", font=("Arial", 12))
        self.crud_menu_btn.grid(row=0, column=1, sticky="nsew", **f2options)

        self.events_btn = tk.Button(self.f2, text="Events", font=("Arial", 12))
        self.events_btn.grid(row=0, column=2, sticky="nsew", **f2options)

        self.reports_btn = tk.Button(self.f2, text="Reports", font=("Arial", 12))
        self.reports_btn.grid(row=0, column=3, sticky="nsew", **f2options)