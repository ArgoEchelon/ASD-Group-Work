#Zak Kannemeyer 22021286

from model.main import Model
from views.main import View
from views.create_order import CreateOrderView
from views.payment import PaymentView
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring

class PaymentController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[PaymentView]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.back_btn.config(command=self.back_btn)
        self.frame.finalize_btn.config(command=self.finalize_btn)
        self.frame.discount_btn.config(command=self.discount_btn)

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
            self.frame.header.config(text=f"Table {tableid} payment")
            self.frame.clear_list()
            self.get_table_orders()
            self.frame.update_totals()
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")
    
    def back_btn(self):
        self.view.switch(CreateOrderView)
        self.maincontroller.create_order_controller.update_view(self.model.tables.current_table)
        self.frame.clear_list()


    def get_table_orders(self):
        #order_ids = self.model.tables.tables[self.model.tables.current_table].current_orders
        orders = self.model.orderManage.get_table_orders(self.model.tables.current_table)
        self.frame.display_items(orders)

    def finalize_btn(self):
        self.model.tables.orders_paid()
        self.frame.discount_var.set(0)
        self.view.payment_message = showinfo("Payment", "PAYMENT PROCESSED !")
        self.back_btn()

    def discount_btn(self):
        discount = askstring('Discount', 'Enter discount %')
        if float(discount) < 0 or float(discount) > 100: 
            self.view.error_message = showerror("Error", "INVALID DISCOUNT PERCENTAGE")
        else:
            self.view.info_message = showinfo("Discount", "DISCOUNT APPLIED")
            self.frame.discount_var.set(float(discount))
            self.frame.update_totals()
        