class B503020:
    def necesities(self, a):
        return a*.5

    def wants(self, a):
        return a*.3

    def savingsAndDebtRepayment(self, a):
        return a*.2

class B702010:
    def necesities(self, a):
        return a*.7

    def wants(self, a):
        return a*.2

    def savingsAndDebtRepayment(self, a):
        return a*.1

#create a calculator object
b503020 = B503020()
b702010 = B702010()

while True:

    print("1: Would you like your budget in 503020")

    print("2: Would you like your budget in 702010")

    b = int(input("Please select which budget calculator you would like to use"))

    if b == 1:
        print("1: Necesities")
        print("2: Wants")
        print("3: Savings and Debt Repayment")

        ch = int(input("Select financial statement: "))

        #Make sure the user have entered the valid choice
        if ch in (1, 2, 3):

            #first check whether user want to exit
            if(ch == 3):
                break

                #If not then ask fo the input and call appropiate methods
                a = int(input("Please enter your income "))

                if(ch == 1):
                    print(b503020.necesities(a))
                elif(ch == 2):
                    print(b503020.wants(a))
                elif(ch == 3):
                    print(b503020.savingsAndDebtRepayment(a))

        else:
            print("Invalid Input")
    elif b == 2:
        print("1: Necesities")
        print("2: Wants")
        print("3: Savings and Debt Repayment")

        ch = int(input("Select financial statement: "))

        #Make sure the user have entered the valid choice
        if ch in (1, 2, 3):

            #first check whether user want to exit
            if(ch == 3):
                break

                #If not then ask fo the input and call appropiate methods
                a = int(input("Please enter your income "))

                if(ch == 1):
                    print(b702010.necesities(a))
                elif(ch == 2):
                    print(b702010.wants(a))
                elif(ch == 3):
                    print(b702010.savingsAndDebtRepayment(a))

        else:
            print("Invalid Input")
