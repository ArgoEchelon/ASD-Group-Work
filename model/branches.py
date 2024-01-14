#Jack Wemyss 22027196
from DataAccessObject import *

class BranchManagement():
    def __init__(self):
        self.branches = []
        self.get_branches()
        self.current_branch = None
    
    def get_branches(self):
        con = getConn()
        c = getCursor()
        query = 'SELECT restaurantId FROM restaurant;'
        c.execute(query)
        record = c.fetchall()
        for branch in record:
            self.branches.append(Branch(branch[0]))




class Branch():
    def __init__(self, branchid):
        self.branch_id = branchid