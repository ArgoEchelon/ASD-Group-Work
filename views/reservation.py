#Jack Wemyss 22027196
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from DataAccessObject import *

class ReservationView(ttk.Frame):
    reserve_id = 0
    selected_table = None
    time_selected = 0
    customer_name = None
    selected_date = None
    def __init__(self):
        super().__init__()
        #main frame
        self.config(style="MainFrame.TFrame")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        #self.rowconfigure(2, weight=1)
        
        #header frame
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

        self.header = ttk.Label(self.f1, text="Table Booking", font=("Arial", 30), anchor="center")
        self.header.grid(column=2, row=1, sticky="nsew", columnspan=1)

        self.staffname_label = ttk.Label(self.f1, text="Operator: placeholder", font=("Arial", 10), anchor="center")
        self.staffname_label.grid(column=4, row=0, sticky="sw")

        self.staffid_label = ttk.Label(self.f1, text="ID: placeholder", font=("Arial", 10), anchor="center")
        self.staffid_label.grid(column=4, row=1, sticky="nw")

        
        #name and date
        self.f3 = ttk.Frame(self)
        self.f3.columnconfigure(0, weight=1, uniform='a')
        self.f3.columnconfigure(1, weight=1, uniform='a')
        self.f3.columnconfigure(2, weight=1, uniform='a')
        self.f3.columnconfigure(3, weight=1, uniform='a')
        self.f3.columnconfigure(4, weight=1, uniform='a')
        self.f3.rowconfigure(0, weight=1)
        self.f3.grid(row=7, columnspan=5)

        #tables
        self.f4 = ttk.Frame(self)
        self.f4.columnconfigure(0, weight=1, uniform='a')
        self.f4.columnconfigure(1, weight=1, uniform='a')
        self.f4.columnconfigure(2, weight=1, uniform='a')
        self.f4.columnconfigure(3, weight=1, uniform='a')
        self.f4.columnconfigure(4, weight=1, uniform='a')
        self.f4.rowconfigure(0, weight=1)
        self.f4.grid(row=4, columnspan=5)

        #table label
        self.f42 = ttk.Frame(self)
        self.f42.columnconfigure(0, weight=1, uniform='a')
        self.f42.rowconfigure(0, weight=1)
        self.f42.grid(row=3, columnspan=5)
        
        #times
        self.f5 = ttk.Frame(self)
        self.f5.columnconfigure(0, weight=1, uniform='a')
        self.f5.columnconfigure(1, weight=1, uniform='a')
        self.f5.columnconfigure(2, weight=1, uniform='a')
        self.f5.columnconfigure(3, weight=1, uniform='a')
        self.f5.columnconfigure(4, weight=1, uniform='a')
        self.f5.rowconfigure(0, weight=1)
        self.f5.grid(row=6, columnspan=5)

        #time label
        self.f52 = ttk.Frame(self)
        self.f52.columnconfigure(0, weight=1, uniform='a')
        self.f52.rowconfigure(0, weight=1)
        self.f52.grid(row=5, columnspan=5)

        self.f6 = ttk.Frame(self)
        self.f6.columnconfigure(0, weight=1, uniform='a')
        self.f6.rowconfigure(0, weight=1)
        self.f6.rowconfigure(0, weight=1)
        self.f6.rowconfigure(0, weight=1)
        self.f6.grid(row=1, columnspan=5)

        self.f7 = ttk.Frame(self)
        self.f7.columnconfigure(0, weight=1, uniform='a')
        self.f7.rowconfigure(0, weight=1)
        self.f7.grid(row=2, columnspan=5)

        #define
        self.time = tk.Label(self.f52, text="Times", width=10, height=2, font=("arial", 20))

        self.table = tk.Label(self.f42, text="Tables", width=10, height=2, font=("arial", 20))


        self.cal = Calendar(self.f3, selectmode="day", year=2024, month=1)
        self.get_date_button = tk.Button(self.f3, text="Get Selected Date")

        self.name_label = tk.Label(self.f3, text="Customer Name:", width=15)
        self.customer_name = tk.Entry(self.f3, width=20)

        self.confirm = tk.Button(self.f3, text="Confirm Booking", width=20, height=5)

        self.table_label = tk.Label(self.f6, text="Table: ")
        self.time_label = tk.Label(self.f6, text="Time: ")
        self.branch_label = tk.Label(self.f6, text="Branch: ")

        #grid
        self.name_label.grid(row=0, column=0, columnspan = 2)
        self.customer_name.grid(row=0, column = 1, columnspan = 3, padx=(50,0), pady=(5,5))

        self.cal.grid(row=1, column = 0, columnspan = 5, pady=(5,0))
        self.get_date_button.grid(row=2, column = 0, columnspan=5)

        self.time.grid(row=0, column = 0, columnspan = 5, pady=(0,0), sticky="nsew")

        self.table.grid(row=0, column = 0, columnspan = 5, pady=(0,0), sticky="nsew")

        self.confirm.grid(row=8, column=0, columnspan=5, pady=(5, 5), padx=(10,10), sticky="nsew")

        self.table_label.grid(row=0, column=0, columnspan=5)
        self.time_label.grid(row=1, column=0, columnspan=5)
        self.branch_label.grid(row=2, column=0, columnspan=5)

    def add_time_buttons(self, frame, time_array, func):
            for i in range(len(time_array)):
                grid_width = 5
                col = i % grid_width
                row = i // grid_width
                mybutton = tk.Button(frame, text=f'Time {time_array[i].time_id}', command=lambda z= time_array[i].time_id :func(z))
                mybutton.grid(row = row, column=col, padx=5, pady=5, sticky="nsew")

    def add_table_buttons(self, frame, table_array, func):
            for i in range(len(table_array)):
                grid_width = 5
                col = i % grid_width
                row = i // grid_width
                mybutton = tk.Button(frame, text=f'Table {table_array[i].table_id}', command=lambda z= table_array[i].table_id :func(z))
                mybutton.grid(row = row, column=col, padx=5, pady=5, sticky="nsew")

    def add_branch_buttons(self, frame, branch_array, func):
            for i in range(len(branch_array)):
                grid_width = 5
                col = i % grid_width
                row = i // grid_width
                mybutton = tk.Button(frame, text=f'Branch {branch_array[i].branch_id}', command=lambda z= branch_array[i].branch_id :func(z))
                mybutton.grid(row = row, column=col, padx=5, pady=5, sticky="nsew")
                