#Zak Kannemeyer 22021286

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo


class CreateOrderView(ttk.Frame):
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

        self.header = ttk.Label(self.f1, text="Tables", font=("Arial", 30), anchor="center")
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

        self.order_frame = tk.Frame(self.f2)
        self.order_frame.columnconfigure(0, weight=1)
        self.order_frame.rowconfigure(0, weight=2)
        self.order_frame.rowconfigure(1, weight=1)
        self.order_frame.grid(column=0, row=0, rowspan=2,columnspan=1, sticky="nsew")

        self.order_list = ttk.Treeview(self.order_frame,columns=("id","item", "price"), show='headings')
        self.order_list["displaycolumns"]=("item", "price")
        self.order_list.heading('price', text='Price')
        self.order_list.heading('item', text='Item')
        self.order_list.grid(column=0, row=0, sticky="nsew", padx=(40,40), pady=(40,0))
        #self.order_list.insert("",'end',values=('fried chimcken borger', '78.00'))

        self.order_function_frame = tk.Frame(self.order_frame)
        self.order_function_frame.columnconfigure(0, weight=1, uniform='a')
        self.order_function_frame.columnconfigure(1, weight=1, uniform='a')
        self.order_function_frame.columnconfigure(2, weight=1, uniform='a')
        self.order_function_frame.rowconfigure(0, weight=1, uniform='a')
        self.order_function_frame.rowconfigure(1, weight=1, uniform='a')
        self.order_function_frame.rowconfigure(2, weight=1, uniform='a')
        self.order_function_frame.grid(column=0, row=1, sticky="nsew")

        self.item_num_label = tk.Label(self.order_function_frame, text="Items: 0", anchor='e')
        self.item_num_label.grid(column=0, row=0, sticky="nsew")

        self.total_price_label = tk.Label(self.order_function_frame, text="Total: £0", anchor='w')
        self.total_price_label.grid(column=2, row=0, sticky="nsew")
        self.total_price = tk.StringVar()

        self.void_item_btn = tk.Button(self.order_function_frame, text="VOID ENTRY", command= self.void_entry)
        self.void_item_btn.grid(column=0, row=1,sticky="nsew")

        self.clear_list_btn = tk.Button(self.order_function_frame, text="CLEAR LIST", command= self.clear_list)
        self.clear_list_btn.grid(column=1, row=1,sticky="nsew")

        self.view_allergens_btn = tk.Button(self.order_function_frame, text="VIEW\nALLERGENS")
        self.view_allergens_btn.grid(column=2, row=1,sticky="nsew")

        self.finish_order_btn = tk.Button(self.order_function_frame, text="FINISH ORDER")
        self.finish_order_btn.grid(column=0, row=2, columnspan=2,sticky="nsew")

        self.table_payment_btn = tk.Button(self.order_function_frame, text="PAYMENT")
        self.table_payment_btn.grid(column=2, row=2,sticky="nsew")



        self.menu_items_frame = ttk.Frame(self.f2)
        self.menu_items_frame.config(style="MainFrame.TFrame")
        self.menu_items_frame.columnconfigure(0, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(1, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(2, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(3, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(4, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(5, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(6, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(7, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(8, weight=1, uniform='a')
        self.menu_items_frame.columnconfigure(9, weight=1, uniform='a')
        self.menu_items_frame.rowconfigure(0, weight=1, uniform='b')
        self.menu_items_frame.rowconfigure(1, weight=1, uniform='b')
        self.menu_items_frame.rowconfigure(2, weight=1, uniform='b')
        self.menu_items_frame.rowconfigure(3, weight=1, uniform='b')
        self.menu_items_frame.rowconfigure(4, weight=1, uniform='b')
        self.menu_items_frame.grid(column=1, row=0, rowspan=2, columnspan=4, sticky="nsew")


    def add_item_buttons(self, frame, menu_array):
        color = {
            'STARTER': '#faad20',
            'MAIN': '#ed4040',
            'SIDE': '#943794',
            'DESSERT': '#4f4fd6',
            'DRINK': '#339133'
        }
            
        for i in range(len(menu_array)):
            grid_width = 10
            col = i % grid_width
            row = i // grid_width
            mybutton = tk.Button(frame,wraplength=120, justify="center", foreground='white', background=color[menu_array[i][3]], text=menu_array[i][1], command=lambda z= menu_array[i] :self.add_item(z))
            mybutton.grid(row = row, column=col, padx=20, pady=20, sticky="nsew")



    
    def add_item(self, item):
        self.order_list.insert("",'end',values=(item))
        print(str(item))
        self.update_totals()
    
    

    def void_entry(self):
        selected_item = self.order_list.selection()
        self.order_list.delete(selected_item)
        self.update_totals()

    def clear_list(self):
        self.order_list.delete(*self.order_list.get_children())
        self.update_totals()

    def update_totals(self):
        self.item_num_label.config(text=f'Items: {len(self.order_list.get_children())}')
        total = 0
        for item in self.order_list.get_children():
            total += float(self.order_list.item(item, 'values')[2])
        
        self.total_price_label.config(text=f'Total: \u00a3{total:,.2f}')    
        self.total_price.set('{:.2f}'.format(total))

  
