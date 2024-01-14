#Jack Wemyss 22027196
from model.main import Model
from views.main import View
from views.home import HomeView
from views.reservation import ReservationView
from DataAccessObject import *
from tkinter.messagebox import showerror, showinfo


class ReservationController:
    def __init__(self, controller, model: Model, view: View) -> None:
        self.maincontroller = controller
        self.model = model
        self.view = view
        self.frame = self.view._frames[ReservationView]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.back_btn.config(command=self.back_btn)
        self.frame.confirm.config(command=self.bookTable)
        self.frame.get_date_button.config(command=self.get_selected_date)
        

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
            self.frame.add_table_buttons(self.frame.f4, self.model.tables.tables, self.selectTable)
            self.frame.add_time_buttons(self.frame.f5, self.model.times.times, self.selectTime)
            self.frame.add_branch_buttons(self.frame.f7, self.model.branches.branches, self.selectBranch)
        else:
            self.frame.staffname_label.config(text=f"")
            self.frame.staffid_label.config(text=f"")

    def table_selected(self, table_id):
        self.view.switch(ReservationView)
        self.maincontroller.reservation_controller.update_view(table_id)

    def time_selected(self, time_id):
        self.view.switch(ReservationView)
        self.maincontroller.reservation_controller.update_view(time_id)

    def branch_selected(self, branch_id):
        self.view.switch(ReservationView)
        self.maincontroller.reservation_controller.update_view(branch_id)
    
    def back_btn(self):
        self.view.switch(HomeView)
        self.maincontroller.home_controller.update_view()

    # will add time and table to db
    def bookTable(self):
        try:
            con = getConn()
            cursor = getCursor()
            if not self.frame.customer_name.get() or not self.selected_date or not self.time_selected or not self.selected_table or not self.branch_selected:
                showerror("Booking unsuccessful", "Please fill in all required fields.")
                return

            overlapping_reservation = self.checkOverlappingReservation(cursor, self.selected_table, self.time_selected, self.selected_date, self.branch_selected)

            if overlapping_reservation:
                showerror("Booking unsuccessful", "The selected table and time are already booked.")
                return

            reserve_id = self.set_reservation_id()
            cursor.execute('INSERT INTO reservation (reservationId, tableId, reservationTimeId, customerName, reservationDate, restaurantId) VALUES (?, ?, ?, ?, ?, ?)', (reserve_id, self.selected_table, self.time_selected, self.frame.customer_name.get(), self.selected_date, self.branch_selected))
            con.commit()

            self.view.error_message = showinfo("Booking successful", f"name: {self.frame.customer_name.get()}, date: {self.selected_date}, time: {self.time_selected}, table: {self.selected_table}, branch: {self.branch_selected}")
            print(f"{self.frame.customer_name.get()} booked table {self.selected_table} for {self.time_selected} on {self.selected_date} at {self.branch_selected}")

            self.selected_table = None
            self.time_selected = 0
            self.frame.customer_name.delete(0, 'end')  # Clear the Entry widget after booking
            self.selected_date = None
            self.branch_selected = None
        except Exception as e:
            print(e)
            showerror("Booking unsuccessful", "An error occurred during booking.")
            
    def checkOverlappingReservation(self, cursor, table_id, time_id, reservation_date, branch_id):
        # Check if there is an existing reservation for the selected table, time, and date
        cursor.execute('SELECT * FROM reservation WHERE tableId = ? AND reservationTimeId = ? AND reservationDate = ? AND restaurantId = ?', 
                       (table_id, time_id, reservation_date, branch_id))
        existing_reservation = cursor.fetchone()

        return existing_reservation is not None
           

    def set_reservation_id(self):
        con = getConn()
        cursor = getCursor()
        query = 'SELECT MAX(reservationId) FROM reservation;'
        cursor.execute(query)
        record = cursor.fetchone()
        
        if record[0] is not None:
            reservationId = record[0] + 1
        else:
            reservationId = 1

        return reservationId


    # function to select the table
    def selectTable(self, table):
        self.selected_table = table
        self.frame.table_label.config(text=f"Table: {table}")

    # function to select the time
    def selectTime(self, time):
        self.time_selected = time
        self.frame.time_label.config(text=f"Table: {time}")

    def selectBranch(self, branch):
        self.branch_selected = branch
        self.frame.branch_label.config(text=f"Branch: {branch}")

    def get_selected_date(self):
        self.selected_date = self.frame.cal.get_date()
