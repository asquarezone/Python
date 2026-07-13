from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount
    
class ReferralDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.95
    
class PremiumCustomerDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.8
    
class CouponCodeDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.92
    

class Checkout:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def checkout(self, amount):
        return self.discount_strategy.apply_discount(amount)
    

if __name__ == "__main__":
    normal_checkout = Checkout(NoDiscount())
    print(f" Normal customer for amount of 1000 => {normal_checkout.checkout(1000)}")

    premium_checkout = Checkout(PremiumCustomerDiscount())
    print(f" Premium customer for amount of 1000 => {premium_checkout.checkout(1000)}")

    