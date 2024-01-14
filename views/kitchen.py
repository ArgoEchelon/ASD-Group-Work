#Leo Gan 22007334
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

class KitchenView(ttk.Frame):
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

        self.header = ttk.Label(self.f1, text="Select Order", font=("Arial", 30), anchor="center")
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
        self.order_frame.rowconfigure(0, weight=3)
        self.order_frame.rowconfigure(1, weight=1)
        self.order_frame.grid(column=0, row=0, rowspan=2,columnspan=1, sticky="nsew")
        
        self.order_list = ttk.Treeview(self.order_frame, columns=("Item", "Quantity"), show='headings')
        self.order_list.heading('Item', text='Item')
        self.order_list.heading('Quantity',text="Quantity")
        self.order_list.column('Item', width=50)
        self.order_list.column('Quantity', width=50)
        self.order_list.grid(column=0, row=0, sticky="nsew", padx=(40,40), pady=(40,0))

        self.order_function_frame = tk.Frame(self.order_frame)
        self.order_function_frame.columnconfigure(0, weight=1, uniform='a')
        self.order_function_frame.columnconfigure(1, weight=1, uniform='a')
        self.order_function_frame.columnconfigure(2, weight=1, uniform='a')
        self.order_function_frame.rowconfigure(0, weight=1, uniform='a')
        self.order_function_frame.rowconfigure(1, weight=1, uniform='a')
        self.order_function_frame.rowconfigure(2, weight=1, uniform='a')
        self.order_function_frame.grid(column=0, row=1, sticky="nsew")

        self.mark_order_btn = tk.Button(self.order_function_frame, text="MARK READY")
        self.mark_order_btn.grid(column=0, row=0, columnspan=3, rowspan= 2, sticky="nsew")

        self.active_orders_frame = ttk.Frame(self.f2)
        self.active_orders_frame.config(style="MainFrame.TFrame")
        self.active_orders_frame.columnconfigure(0, weight=1)
        self.active_orders_frame.columnconfigure(1, weight=1)
        self.active_orders_frame.columnconfigure(2, weight=1)
        self.active_orders_frame.columnconfigure(3, weight=1)
        self.active_orders_frame.columnconfigure(4, weight=1)
        self.active_orders_frame.columnconfigure(5, weight=1)
        self.active_orders_frame.rowconfigure(0, weight=1)
        self.active_orders_frame.rowconfigure(1, weight=1)
        self.active_orders_frame.rowconfigure(2, weight=1)
        self.active_orders_frame.rowconfigure(3, weight=1)
        self.active_orders_frame.grid(column=1, row=0, rowspan=2, columnspan=4, sticky="nsew")

    def add_order_buttons(self, frame, order_array, func, buttons, restaurantId):
        for i in range(len(order_array)):
            grid_width = 6
            col = i % grid_width
            row = i // grid_width
            mybutton = tk.Button(frame, text=f'Order {order_array[i].orderId}', command=lambda z= order_array[i], rid=restaurantId: (func(z.orderId, rid)))
            mybutton.grid(row = row, column=col, padx=50, pady=50, sticky="nsew")
            buttons.append(mybutton)