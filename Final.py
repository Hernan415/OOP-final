#Budgetting


class Budget():
    def __init__(self):
        self.income = self.Income()
        self.expenses = self.Expenses()
        self.emergancyFunds = self.income - self.expenses
        print(self.emergancyFunds)

    class Income():
        def __init__(self):
            self.hourlyPay = int(input("How much is your hourly pay: "))
            self.hoursWorked = int(input("How many hours do you plan on working this month? : "))
            self.paycheck = int(self.hourlyPay * self.hoursWorked)

    class Expenses():
        def __init__(self):
            self.bills = self.Bills()
            self.stocks = self.Stocks()
            self.expenses = int(self.bills + self.stocks)

        class Bills():
            def __init__(self):
                self.food = int(input("How much money do you want to spend on food this month?: "))
                self.rent = int(input("How much is your rent?: "))
                self.utilities = int(input("How much is your utilities bill?: "))
                self.bills = int(self.food + self.rent + self.utilities)

        class Stocks():
            def __init__(self):
                self.dividends = int(input("If you get dividend payment from stocks, how much was this months?: "))
                self.investments = int(input("How much money will you be investing in the stock market this month?: "))
                self.outsideFinancials = int(self.dividends - self.investments)


def monthlyBudget():
    budget = Budget()
monthlyBudget()
