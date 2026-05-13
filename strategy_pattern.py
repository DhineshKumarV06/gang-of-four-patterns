# Payment processing 

from abc import ABC,abstractmethod

class payment_startegy(ABC):

    def pay(self,amount):
        pass

class CreditCard_payment(payment_startegy):

    def pay(self, amount):
        print(f"paid {amount} using credit card")

class UPI_payment(payment_startegy):

    def pay(self, amount):
        print(f"paid {amount} using UPI")

class PayPal_payment(payment_startegy):

    def pay(self, amount):
        print(f"paid {amount} using PayPal")

class shopping_kart:
    def __init__(self,strategy):
        self.startegy=strategy
    def checkout(self,amount):
        self.startegy.pay(amount)
kart=shopping_kart(UPI_payment())
kart.checkout(5000)