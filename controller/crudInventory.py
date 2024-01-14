#Phoenix Burke Chang 21026891

from model.main import Model
from views.main import View
from views.crudInventory import InventoryView
from views.home import HomeView
from tkinter.messagebox import showerror, showinfo

class InventoryController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[InventoryView]
        self._bind()

    def _bind(self) -> None:
        self.frame.back_btn.config(command=self.back_btn)
        self.frame.add_record_btn.config(command=lambda: self.add_record(
            self.frame.stockId.get(),
            self.frame.stockNum.get(),
            self.frame.stockPrice.get()
        ))
        self.frame.del_record_btn.config(command=lambda: self.delete_record(
            self.frame.tree.selection()
        ))

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
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")
        self.query_database()

    def back_btn(self):
        self.view.switch(HomeView)
        self.maincontroller.home_controller.update_view()

    def add_record(self, stockId, stockNum, stockPrice):
        if self.frame.validate_entries():
            restaurantId = self.model.auth.current_restaurantid
            self.model.inventory.add_record(stockId, stockNum, stockPrice, restaurantId)
            self.frame.clear_entries()
            self.frame.tree.delete(*self.frame.tree.get_children())
            self.maincontroller.inventory_controller.update_view()
            self.frame.clear_entries()

    def delete_record(self, selected_item):
        if not selected_item:
            self.view.error_message = showerror("Warning", "Please select a record to delete.")
            return
        restaurantId = self.model.auth.current_restaurantid
        selected_row = self.frame.tree.item(selected_item)
        values = selected_row['values']
        staff_id = values[0]
        self.model.inventory.delete_record(staff_id, restaurantId)
        self.frame.tree.delete(selected_item)
        self.view.error_message = showinfo("Deleted!", "Your Record Has Been Deleted!")
        self.maincontroller.inventory_controller.update_view()

    def query_database(self):
        records = self.model.inventory.query_database()
        for index, record in enumerate(records):
            values = record
            self.frame.tree.insert(parent='', index='end', iid=index, text='', values=values)