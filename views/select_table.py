#Zak Kannemeyer 22021286

import tkinter as tk
from tkinter import ttk


class SelectTableView(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.config(style="MainFrame.TFrame")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)
        #self.rowconfigure(2, weight=1)
        
        self.f1 = ttk.Frame(self)
        self.f1.columnconfigure(0, weight=1, uniform='a')
        self.f1.columnconfigure(1, weight=1, uniform='a')
        self.f1.columnconfigure(2, weight=1, uniform='a')
        self.f1.columnconfigure(3, weight=1, uniform='a')
        self.f1.columnconfigure(4, weight=1, uniform='a')
        self.f1.rowconfigure(0, weight=1)
        self.f1.grid(row=0, sticky="nwes")

        self.back_btn = tk.Button(self.f1, text="Back", font=("Arial", 15))
        self.back_btn.grid(column=0, row=0, rowspan=2, columnspan=1, sticky="nsew")

        self.header = ttk.Label(self.f1, text="Select Table", font=("Arial", 30), anchor="center")
        self.header.grid(column=2, row=1, sticky="nsew", columnspan=1)

        self.staffname_label = ttk.Label(self.f1, text="Operator: placeholder", font=("Arial", 10), anchor="center")
        self.staffname_label.grid(column=4, row=0, sticky="sw")

        self.staffid_label = ttk.Label(self.f1, text="ID: placeholder", font=("Arial", 10), anchor="center")
        self.staffid_label.grid(column=4, row=1, sticky="nw")


        self.f2 = ttk.Frame(self)
        #f2options = {'padx': 15, 'pady': 15}
        self.f2.config(style="MainFrame.TFrame")
        self.f2.columnconfigure(0, weight=1, uniform='a')
        self.f2.columnconfigure(1, weight=1, uniform='a')
        self.f2.columnconfigure(2, weight=1, uniform='a')
        self.f2.columnconfigure(3, weight=1, uniform='a')
        self.f2.columnconfigure(4, weight=1, uniform='a')
        self.f2.rowconfigure(0, weight=1, uniform='c')
        self.f2.rowconfigure(1, weight=1, uniform='c')
        self.f2.grid(row=1, sticky="nsew", pady=(0, 0))


        self.tables_frame = ttk.Frame(self.f2)
        self.tables_frame.config(style="MainFrame.TFrame")
        self.tables_frame.columnconfigure(0, weight=1)
        self.tables_frame.columnconfigure(1, weight=1)
        self.tables_frame.columnconfigure(2, weight=1)
        self.tables_frame.columnconfigure(3, weight=1)
        self.tables_frame.columnconfigure(4, weight=1)
        self.tables_frame.columnconfigure(5, weight=1)
        self.tables_frame.columnconfigure(6, weight=1)
        self.tables_frame.columnconfigure(7, weight=1)
        self.tables_frame.columnconfigure(8, weight=1)
        #self.tables_frame.columnconfigure(9, weight=1)
        self.tables_frame.rowconfigure(0, weight=1)
        self.tables_frame.rowconfigure(1, weight=1)
        self.tables_frame.rowconfigure(2, weight=1)
        self.tables_frame.rowconfigure(3, weight=1)
        self.tables_frame.rowconfigure(4, weight=1)
        self.tables_frame.grid(column=0, row=0, rowspan=2, columnspan=5, sticky="nsew")



    def add_table_buttons(self, frame, table_array, func):
            
        for i in range(len(table_array)):
            grid_width = 9
            col = i % grid_width
            row = i // grid_width
            mybutton = tk.Button(frame, text=f'Table {table_array[i].table_id}', command=lambda z= table_array[i].table_id :func(z))
            mybutton.grid(row = row, column=col, padx=50, pady=50, sticky="nsew")



        