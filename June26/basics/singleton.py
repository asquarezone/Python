import threading
class CurrencyConvertor:
    instance = None
    lock = threading.Lock()

    def __new__(cls):
        print("1. __new__ called")
        if cls.instance is not None:
            return CurrencyConvertor.instance
        with cls.lock:
            if cls.instance is not None:
                return CurrencyConvertor.instance
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("inside init")

    def convert(self, value, source_currency, destination_currency):
        pass


if __name__ == '__main__':
    c1 = CurrencyConvertor()
    c2 = CurrencyConvertor()
    print(c1 == c2)
