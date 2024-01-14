#Zak Kannemeyer 22021286

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring


class PaymentView(ttk.Frame):
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

        self.header = ttk.Label(self.f1, text="PAYMENT FRAME", font=("Arial", 30), anchor="center")
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
        self.f2.rowconfigure(0, weight=1, uniform='b')
        self.f2.rowconfigure(1, weight=1, uniform='b')
        self.f2.rowconfigure(2, weight=1, uniform='b')
        self.f2.rowconfigure(3, weight=1, uniform='b')
        #self.f2.rowconfigure(1, weight=1, uniform='b')
        self.f2.grid(row=1, sticky="nsew", pady=(0, 0))
        

        self.item_list = ttk.Treeview(self.f2,columns=("order","item","quantity", "price"), show='headings')
        
        self.item_list.heading('price', text='Price')
        self.item_list.heading('order', text='Order#')
        self.item_list.heading('item', text='Item')
        self.item_list.heading('quantity', text='Quantity')
        self.item_list.grid(column=1, columnspan=2, row=0, rowspan=3, sticky="nsew", pady=30)

        self.function_frame = ttk.Frame(self.f2)
        self.function_frame.columnconfigure(0, weight=1)
        self.function_frame.rowconfigure(0, weight=1, uniform='c')
        self.function_frame.rowconfigure(1, weight=1, uniform='c')
        self.function_frame.rowconfigure(2, weight=1, uniform='c')
        self.function_frame.rowconfigure(3, weight=1, uniform='c')
        self.function_frame.rowconfigure(4, weight=1, uniform='c')
        self.function_frame.rowconfigure(5, weight=1, uniform='c')
        self.function_frame.rowconfigure(6, weight=1, uniform='c')
        self.function_frame.grid(column=3, row=0, rowspan=3, sticky="nsew", pady=30)

        self.subtotal_frame = tk.LabelFrame(self.function_frame, text='SUBTOTAL', font=(None,30))
        self.subtotal_frame.grid(row=0, column=0, sticky='nsew')

        self.subtotal_amount = tk.Label(self.subtotal_frame, text='\u00a30.00', font=(None,30))
        self.subtotal_amount.place(relx=.5, rely=.5,anchor= 'center')

        self.discount_frame = tk.LabelFrame(self.function_frame, text='DISCOUNT', font=(None,30))
        self.discount_frame.grid(row=1, column=0, sticky='nsew')

        self.discount_amount = tk.Label(self.discount_frame, text='%0.0', font=(None,30))
        self.discount_amount.place(relx=.5, rely=.5,anchor= 'center')

        self.total_frame = tk.LabelFrame(self.function_frame, text='TOTAL', font=(None,30))
        self.total_frame.grid(row=2, column=0, sticky='nsew')

        self.total_amount = tk.Label(self.total_frame, text='\u00a30.00', font=(None,30))
        self.total_amount.place(relx=.5, rely=.5,anchor= 'center')



        self.discount_btn = tk.Button(self.function_frame, text=' APPLY DISCOUNT')
        self.discount_btn.grid(row=5, column=0, sticky='nsew')

        self.finalize_btn = tk.Button(self.function_frame, text='FINALIZE PAYMENT')
        self.finalize_btn.grid(row=6, column=0, sticky='nsew')

        self.discount_var = tk.IntVar()
        self.discount_var.set(0)



    def display_items(self, orders):
        for item in orders:
            self.item_list.insert("",'end',values=(item))
        
    def clear_list(self):
        self.item_list.delete(*self.item_list.get_children())
    
    def update_totals(self):
        subtotal = 0
        for item in self.item_list.get_children():
            subtotal += float(self.item_list.item(item, 'values')[3])
        
        discount = self.discount_var.get()
        print(f'discount{discount} yuh')
        print(type(discount))
        total = subtotal - (subtotal *(discount/100))
        
        
        self.subtotal_amount.config(text=f'\u00a3{subtotal:,.2f}')
        self.discount_amount.config(text=f'%{discount:,.1f}')
        self.total_amount.config(text=f'\u00a3{total:,.2f}')


        #self.total_price.set('{:.2f}'.format(total))



    
