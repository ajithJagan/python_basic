from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def credit(self):
        pass
    @abstractmethod
    def debit(self):
        pass
    

class SBI(RBI):
    def credit(self):
        print("SBI credit card")
    def debit(self):
        print("SBI debit card")
    def balance(self):
        print("SBI balance")

obj = SBI()
obj.credit()
obj.debit()
obj.balance()