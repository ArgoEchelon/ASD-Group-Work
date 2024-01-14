#Leo Gan 22007334
from model.main import Model
from views.main import View
from views.kitchen import KitchenView
from views.login import LogInView
from views.home import HomeView
from tkinter.messagebox import showerror, showinfo

class KitchenController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[KitchenView]
        self.buttons = []
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.back_btn.config(command=self.back_btn)
        self.frame.mark_order_btn.config(command=self.mark_order_btn)
    
    def update_view(self) -> None:
        current_firstname = self.model.auth.current_firstname
        current_lastname = self.model.auth.current_lastname
        current_staffid = self.model.auth.current_staffid
        if current_staffid:
            firstname = current_firstname
            lastname = current_lastname
            staffid = current_staffid
            self.frame.staffname_label.config(text=f"Operator: {firstname} {lastname}")
            self.frame.staffid_label.config(text=f"ID: {staffid}")
            orders = self.model.orderManage.get_orders(self.model.auth.current_restaurantid)
            self.buttons.clear
            self.frame.add_order_buttons(self.frame.active_orders_frame, orders , self.order_selected, self.buttons, self.model.auth.current_restaurantid)
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")
        

    
    def order_selected(self, order_id, restaurantId):
        self.frame.order_list.delete(*self.frame.order_list.get_children())
        self.model.orderManage.current_order = order_id
        details = self.model.orderManage.get_order_details(order_id, restaurantId)
        for detail in details:
            self.frame.order_list.insert("",'end',values=(detail.itemName, detail.quantity))

    def mark_order_btn(self):
        order_id = self.model.orderManage.current_order
        self.view.order_complete_message = showinfo("Order", "Order Ready!")
        self.model.orderManage.mark_order(order_id)
        self.frame.order_list.delete(*self.frame.order_list.get_children())
        for button in self.buttons:
            button.destroy()
        self.buttons.clear()
        self.frame.after(30, self.update_view) # Schedule next update

    def back_btn(self):
        for button in self.buttons:
            button.destroy()
        self.buttons.clear()
        self.view.switch(HomeView)
        self.maincontroller.home_controller.update_view()