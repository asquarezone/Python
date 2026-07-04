from abc import ABC, abstractmethod


class Checkout(ABC):

    # method template
    def place_order(self):
        self.validate_cart()
        self.calculate_total()
        self.process_payment()
        self.generate_invoice()
        self.send_confirmation()

    def validate_cart(self):
        print("Validating cart")

    def calculate_total(self):
        print("Calculating total")

    @abstractmethod
    def process_payment(self):
        pass

    def generate_invoice(self):
        print("Generating invoice")

    def send_confirmation(self):
        print("Sending confirmation")


class CreditCardCheckout(Checkout):

    def process_payment(self):
        print("Charging credit card")


class PhonePeCheckout(Checkout):

    def process_payment(self):
        print("Processing Phonepe payment")


if __name__ == "__main__":
    #my_checkout = CreditCardCheckout()
    #my_checkout.place_order()
    your_checkout = PhonePeCheckout()
    your_checkout.place_order()
    #checkout = Checkout() #error



