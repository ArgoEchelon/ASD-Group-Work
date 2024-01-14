#Phoenix Burke Chang 21026891

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class InventoryView(ttk.Frame):
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

        self.header = ttk.Label(self.f1, text="CRUD Inventory", font=("Arial", 30), anchor="center")
        self.header.grid(column=2, row=1, sticky="nsew", columnspan=1)

        self.staffname_label = ttk.Label(self.f1, text="Operator: placeholder", font=("Arial", 10), anchor="center")
        self.staffname_label.grid(column=4, row=0, sticky="sw")

        self.staffid_label = ttk.Label(self.f1, text="ID: placeholder", font=("Arial", 10), anchor="center")
        self.staffid_label.grid(column=4, row=1, sticky="nw")




        self.f2 = ttk.Frame(self)
        self.f2.config(style="MainFrame.TFrame")
        self.f2.columnconfigure(0, weight=1, uniform='a')
        self.f2.columnconfigure(1, weight=1, uniform='a')
        self.f2.columnconfigure(2, weight=1, uniform='a')
        self.f2.columnconfigure(3, weight=1, uniform='a')
        self.f2.columnconfigure(4, weight=1, uniform='a')
        self.f2.rowconfigure(0, weight=1, uniform='c')
        self.f2.rowconfigure(1, weight=1, uniform='c')
        self.f2.grid(row=1, sticky="ew", pady=(30, 0))



        self.tree = ttk.Treeview(self.f2, columns=('stock_Id', 'stock_Num', 'stock_Price'), show='headings')
        self.tree.heading('stock_Id', text='Stock ID List')
        self.tree.heading('stock_Num', text='Stock Amount List')
        self.tree.heading('stock_Price', text='Stock Price List')

        #change to sql query
        #contacts = [(f'Staff ID {n}', f'password {n}', f'first {n}', f'last {n}') for n in range(1, 100)]
        #for contact in contacts:
            #self.tree.insert('', tk.END, values=contact)

        self.tree.grid(row=0, column=1, sticky="nsew", columnspan=2)

        self.scrollbar = ttk.Scrollbar(self.f2, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.grid(row=0, column=3, sticky="wns")
        self.tree.configure(yscroll=self.scrollbar.set)

        self.f3 = ttk.Frame(self)
        self.f3.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.stockId = tk.StringVar()
        self.stockNum = tk.StringVar()
        self.stockPrice = tk.StringVar()

        ttk.Label(self.f3, text='Stock ID:', font=("Arial", 12)).grid(column=0, row=0, sticky=tk.W, padx=15, pady=5)
        ttk.Entry(self.f3, textvariable=self.stockId, font=("Arial", 12)).grid(column=1, row=0, sticky=tk.E, padx=15, pady=5)

        ttk.Label(self.f3, text='Stock Amount:', font=("Arial", 12)).grid(column=0, row=1, sticky=tk.W, padx=15, pady=5)
        ttk.Entry(self.f3, textvariable=self.stockNum, font=("Arial", 12)).grid(column=1, row=1, sticky=tk.E, padx=15, pady=5)

        ttk.Label(self.f3, text='Stock Price:', font=("Arial", 12)).grid(column=0, row=2, sticky=tk.W, padx=15, pady=5)
        ttk.Entry(self.f3, textvariable=self.stockPrice, font=("Arial", 12)).grid(column=1, row=2, sticky=tk.E, padx=15, pady=5)

        self.add_record_btn = tk.Button(self.f3, text='Add Record', font=("Arial", 12))
        self.add_record_btn.grid(column=0, row=5, sticky=tk.E, padx=15, pady=5)
        self.del_record_btn = tk.Button(self.f3, text='Delete Record', font=("Arial", 12))
        self.del_record_btn.grid(column=1, row=5, sticky=tk.E, padx=15, pady=5)

    def clear_entries(self):
        self.stockId.set('')
        self.stockNum.set('')
        self.stockPrice.set('')
    
    def validate_entries(self):
        # Validate staffId and password
        for entry_var, entry_name, max_length in [
            (self.stockId, "Staff ID", 4),
            (self.stockNum, "Stock Amount", 4),
            (self.stockPrice, "First Name", 20)
        ]:
            value = entry_var.get()

            # Check for empty or exceeding max length
            if not value or len(value) > max_length:
                messagebox.showwarning("Invalid Input", f"{entry_name} must not be empty and should have a maximum length of {max_length} characters.")
                return False

            # Check for digits for staffId and password
            if entry_name in ["Stock ID", "Password"] and (not value.isdigit() or len(value) != 4):
                messagebox.showwarning("Invalid Input", f"{entry_name} must be a 4-digit number.")
                return False
        return True