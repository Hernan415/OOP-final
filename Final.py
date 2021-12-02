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

#class Investments:

#class Percentage

def budget():
    income = Income()
    bills = Bills()

    #investments = Investments()
    #percentage = Percentage


budget()
