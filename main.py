# imports
from datetime import datetime

# classes

class Theater:
    def __init__(self, seatNum, seatType):
        self.seatNum = seatNum
        # Balcony and Ordinary seats
        self.seatType = seatType
        self.transactionID = None
        self.allotmentStatus = False

    def allot(self, ID):
        self.allotmentStatus = True
        self.transactionID = ID

    def isAvailable(self):
        return not self.allotmentStatus

    def cancel(self):
        self.allotmentStatus = False
        self.transactionID = None

class Seat:

class Show:

class ShowManager:

class Salesperson:

class Spectator:

class AccountsClerk:

class Transaction:

class Ledger:

class ManagementSystem:

