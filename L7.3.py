class ATM:
    def __init__(self, bankName, bankAddress):
        self.__bankName = bankName
        self.__bankAddress = bankAddress

    def activateCashDispenser(self):
        print("Cash Dispensed")
    def printReceipt(self):
        print("Receipt Printed")

class Account:
    def __init__(self, accountNumber, balance):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        print("Cash Balance is: " + self.__balance)

class Customer:
    def __init__(self, name, address, account):
        self.__name = name
        self.__address = address
        self.__account = account

    def deposit(self):
        float(input("How much would you like to deposit? (In $)"))
    def withdraw(self):
        float(input("How much would you like to withdraw? (In $)"))
    def checkBalance(self):
        return self.__balance

