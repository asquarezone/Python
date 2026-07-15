from abc import ABC, abstractmethod
from gst import GST

class BaseSingleOperation(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class AddOperation(BaseSingleOperation):
    def execute(self, *args):
        result = 0
        for i in args:
            result += i
        return result
    
class SubtractOperation(BaseSingleOperation):
    def execute(self, *args):
        result = args[0]
        for i in args[1:]:
            result -= i
        return result
    
class GSTAdaptor(BaseSingleOperation):
    def __init__(self):
        self.gst = GST()
    def execute(self, *args):
        # calling the other code
        return self.gst.calculate(*args)
# implement calculator
class Calculator:
    def __init__(self):
        self.operations = {
            'add': AddOperation(),
            'subtract': SubtractOperation(),
            'gst': GSTAdaptor(),
        }

    def calculate(self, operation, *args):
        if operation not in self.operations:
            raise ValueError(f"Unknown operation: {operation}")
        return self.operations[operation].execute(*args)
    
if __name__ == "__main__":
    calc = Calculator()
    print(calc.calculate('add', 1, 2, 3, 4, 5))
    print(calc.calculate('subtract', 10, 2, 3))
    print(calc.calculate('gst', 100))
