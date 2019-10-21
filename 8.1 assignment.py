#myParentClass
class BankAcount():
    def __init__(self, balance, fees):
        self.balance = balance
        self.fees = fees
     def deposit(self):
        amount = float(input("Enter amount to be deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:", amount)
        
    def withdraw(self): 
        amount = float(input("Enter amount to be withdrawn: ")) 
        if self.balance >= amount: 
            self.balance -= amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ")
     def display(self): 
        print("\n Net Available Balance=",self.balance)
    
# creating an object of class 
s = Bank_Account() 
   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 
    def getBankAcount(self, balance):
        return balance.fees + "" + balance.interestrate + " has " + str(minimumbalance)
#my 1st Child class
class CheckingAccount(BankAcount):
    def __init__(self, AccountNumber, balance, fees, interestrate, minimumbalance):
        BankAcount.__init__(self, balance, fees, interestrate, minimumbalance)
        self.balance = balance
        self.fees = fess
        self.insterestrate = insterestrate
        self.minimumbalance = minimumbalance
     def dedudctFees():
         float(input("Enter amount of fees: ")) 
        self.balance += amount 
        print("\n Amount Fees:", amount)
    def checkMinimumBalance():
        try:
           amount = float(input("Enter Minimum Balance amount : "))
           self.balance >= amount
           self.balance -= amount 
        except:
            print("error in bank account class")
            balance=int(input("Enter you balance"))
        if(balance<50):
            obj1= MinimumBalance()
            print(obj1.message)
        else:
            obj2= BankAccount(balance)

    def getSavingAccount(balance):
        return balance.getFees() + "And it has" + str(minimumbalance) + "minimum balance."
         
#my2ndchildclass
class SavingAccount(BankAcount):
    def __init__(self, balance, interestrate):
        Balance.__init__(self, balance, interestrate)
        self.balance = balance
        self.interestrate = interestrate
     def interestrate(self):
        amount = float(input("Enter amount of interest: ")) 
        self.balance += amount 
        print("\n Amount interst:", amount)
    def getSavingAccount(balance):
        return balance.interestrate + "And it has" + balance.interestrate + " has " + str(minimumbalance)
        
