#Phoenix Burke Chang 21026891
#Zak Kannemeyer 22021286
#Leo Gan 22007334 
import tkinter as tk
from tkinter import ttk


class HomeView(ttk.Frame):
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

        self.signout_btn = tk.Button(self.f1, text="Sign Out", font=("Arial", 15))
        self.signout_btn.grid(column=0, row=0, rowspan=2, columnspan=2, sticky="nsew", padx=(0, 150))

        self.header = ttk.Label(self.f1, text="Horizon Restaurant: placeholder", font=("Arial", 30), anchor="center")
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

        self.create_order_btn = tk.Button(self.f2, text="Create Order", font=("Arial", 12))
        self.create_order_btn.grid(row=0, column=1, sticky="nsew", **f2options)

        self.reservation_btn = tk.Button(self.f2, text="Reservation", font=("Arial", 12))
        self.reservation_btn.grid(row=0, column=2, sticky="nsew", **f2options)

        self.inventory_btn = tk.Button(self.f2, text="Inventory", font=("Arial", 12))
        self.inventory_btn.grid(row=0, column=3, sticky="nsew", **f2options)

        self.manager_func_btn = tk.Button(self.f2, text="Manager Functions", font=("Arial", 12))
        self.manager_func_btn.grid(row=1, column=1, sticky="nsew", **f2options)

        self.admin_func_btn = tk.Button(self.f2, text="Admin Functions", font=("Arial", 12))
        self.admin_func_btn.grid(row=1, column=2, sticky="nsew", **f2options)

        self.kitchen_btn = tk.Button(self.f2, text="Kitchen", font=("Arial", 12))
        self.kitchen_btn.grid(row=1, column=3, sticky="nsew", **f2options)