from abc import ABC, abstractmethod

# Interface equivalent
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Card payment
class CardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs {amount} using Card")


# UPI payment
class UpiPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs {amount} using UPI")


# Cash payment
class CashPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid Rs {amount} using Cash")


# Checkout class
class Checkout:

    def make_payment(self, payment_method: PaymentMethod, amount):
        payment_method.pay(amount)


# Main execution
if __name__ == "__main__":

    checkout = Checkout()

    card = CardPayment()
    upi = UpiPayment()
    cash = CashPayment()

    checkout.make_payment(card, 150000)
    checkout.make_payment(upi, 999)
    checkout.make_payment(cash, 555)
