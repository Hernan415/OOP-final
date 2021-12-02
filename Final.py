#Budgetting



class Income():
    def __init__(self):
        self.hourlyPay = int(input("How much is your hourly pay: "))
        self.hoursWorked = int(input("How many hours do you plan on working this month? : "))
        self.paycheck = self.hourlyPay * self.hoursWorked

class Bills:
    def __init__(self):
        self.food = int(input("How much money do you want to spend on food this month?: "))
        self.rent = int(input("How much is your rent?: "))
        self.utilities = int(input("How much is your utilities bill?: "))
        self.expenses = self.food + self.rent + self.utilities

class Stocks:
    def __init__(self):
        self.dividends = int(input("If you get dividend payment from stocks, how much was this months?: "))
        self.investments = int(input("How much money will you be investing in the stock market this month?: "))
        self.outsideFinancials = self.dividends - self.investments

class Percentage:
    def __init__(self):
        



def budget():
    income = Income()
    bills = Bills()
    stocks = Stocks()
    percentage = Percentage()


budget()
