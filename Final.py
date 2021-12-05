#Budgetting


class Budget():
    def __init__(self):
        self.income = self.Income()
        self.expenses = self.Expenses()
        self.calculateEmergancyFunds()

    def calculateEmergancyFunds(self):
        self.calculateEmergancyFunds = (
            self.income.calculatePaycheck - self.expenses.expenses
            )
            
        print("You have the following as disposable income this month:")
        print(self.calculateEmergancyFunds)

    class Income():
        def __init__(self):
            self.hourlyPay = int(input("How much is your hourly pay: "))
            self.hoursWorked = int(input("How many hours do you plan on working this month? : "))
            self.calculatePaycheck()

        def calculatePaycheck(self):
            self.calculatePaycheck = (
                int(self.hourlyPay * self.hoursWorked)
                )

    class Expenses():
        def __init__(self):
            self.bills = self.Bills()
            self.stocks = self.Stocks()
            self.calculateExpenses()

        def calculateExpenses(self):
            self.expenses = (
                self.bills.bills + self.stocks.stocks
                )

        class Bills():
            def __init__(self):
                self.food = int(input("How much money do you want to spend on food this month?: "))
                self.rent = int(input("How much is your rent?: "))
                self.utilities = int(input("How much is your utilities bill?: "))
                self.calculateBills()
                self.calculateNecesities()

            def calculateBills(self):
                self.bills = (
                    int(self.food + self.rent + self.utilities)
                    )
            def calculateNecesities(self):
                self.necesities = (
                    int(self.food + self.rent)
                )

        class Stocks():
            def __init__(self):
                self.dividends = int(input("If you get dividend payment from stocks, how much was this months?: "))
                self.investments = int(input("How much money will you be investing in the stock market this month?: "))
                self.calculateStocks()

            def calculateStocks(self):
                self.stocks = (
                    int(self.dividends - self.investments)
                    )

def monthlyBudget():
    budget = Budget()
monthlyBudget()
