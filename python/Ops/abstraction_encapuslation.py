
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance 

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def __str__(self): 
        return f"The balance is {self.__balance}"  # this is the way to print the balance

MyBalance = 1000

obj = BankAccount(MyBalance)
# print(obj.get_balance())
# obj.deposit(1000)
# print(obj.get_balance())
# obj.withdraw(1000)
# print(obj.get_balance())

print(obj)

