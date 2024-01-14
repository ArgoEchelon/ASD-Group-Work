#Jack Wemyss 22027196
from DataAccessObject import *

class TimeManagement():
    def __init__(self):
        self.times = []
        self.get_times()
        self.current_time = None
    
    def get_times(self):
        con = getConn()
        c = getCursor()
        query = 'SELECT timeSlots FROM reservationTimes;'
        c.execute(query)
        record = c.fetchall()
        for time in record:
            self.times.append(Time(time[0]))




class Time():
    def __init__(self, timeid):
        self.time_id = timeid


