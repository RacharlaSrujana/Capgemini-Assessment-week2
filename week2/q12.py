'''Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment`
   that override the method differently.'''

class Payment:
    def process_payment(self):
        print("The payment can be done through different wways")
class CreditCardPayment(Payment):
    def process_payment(self):
        super().process_payment()
        print("The payment is done using credit card")
class PayPalPayment(Payment):
    def process_payment(self):
        print("The payment is done using Paypal")
class BitCoinPayment(Payment):
    def process_payment(self):
        print("The payment is done using Bitcoin")
c=CreditCardPayment()
c.process_payment()
p=PayPalPayment()
p.process_payment()
b=BitCoinPayment()
b.process_payment()