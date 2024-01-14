#Zak Kannemeyer 22021286

from model.main import Model
from views.main import View
from views.create_order import CreateOrderView
from views.select_table import SelectTableView
from views.payment import PaymentView
from collections import Counter
from tkinter.messagebox import showerror, showinfo

class CreateOrderController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[CreateOrderView]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.back_btn.config(command=self.back_btn)
        self.frame.finish_order_btn.config(command=self.finish_order_btn)
        self.frame.table_payment_btn.config(command=self.payment_btn)
        self.frame.view_allergens_btn.config(command=self.view_allergens)

    def update_view(self, tableid) -> None:
        current_firstname = self.model.auth.current_firstname
        current_lastname = self.model.auth.current_lastname
        current_staffid = self.model.auth.current_staffid
        if current_staffid:
            firstname = current_firstname
            lastname = current_lastname
            staffid = current_staffid
            self.frame.staffname_label.config(text=f"Operator: {firstname} {lastname}")
            self.frame.staffid_label.config(text=f"ID: {staffid}")
            self.frame.header.config(text=f"Table {tableid}")
            self.frame.add_item_buttons(self.frame.menu_items_frame, self.model.menu.menu_items)
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")
    
    def back_btn(self):
        self.frame.clear_list()
        self.frame.update_totals()
        self.view.switch(SelectTableView)
        self.maincontroller.select_table_controller.update_view()

    def finish_order_btn(self):
        order_entry = self.frame.order_list
        order = []
        for item in order_entry.get_children():
            order.append(order_entry.item(item, 'values')[0])
        if len(order) > 0:
            item_counter = Counter(order)
            #print(order)
            #print(Counter(order))
            prices = self.model.menu.get_prices(item_counter)
            restaurantid= self.model.auth.current_restaurantid
            #print(restaurantid)
            #print(type(restaurantid))

            self.model.tables.create_order(item_counter, prices, restaurantid)
            self.frame.clear_list()
            self.frame.update_totals()
            self.view.order_complete_message = showinfo("Order", "Order Complete !")
            
        else: 
            self.view.order_empty_message = showerror("Order Error", "Order is empty !")

    def view_allergens(self):
        selected_item = self.frame.order_list.selection()
        if len(selected_item) == 1:

            values = self.frame.order_list.item(selected_item, 'values')
            self.view.allergens_message = showinfo("Allergens", values[4])

        else:
            self.view.error_message = showerror("Error", "No item selected!")

    def payment_btn(self):
        #if len(self.model.tables.tables[self.model.tables.current_table].current_orders) > 0:
        self.frame.clear_list()
        self.frame.update_totals()
        self.view.switch(PaymentView)
        self.maincontroller.payment_controller.update_view(self.model.tables.current_table)
        #else:
        #    self.view.error_message = showerror("Error", "There are no outstanding payments !")


        