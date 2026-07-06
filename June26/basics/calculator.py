from abc import ABC, abstractmethod

class BaseSingleResultOperation(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self, *args):
        pass

class Addition(BaseSingleResultOperation):
    def execute(self, *args):
        result = 0
        for i in args:
            result += i
        return result
    
class SimpleIntrest(BaseSingleResultOperation):
    def execute(self, *args):
        p = args[0]
        t = args[1]
        r = args[2]
        return (p*t*r)/100
    
class CompoundIntrest(BaseSingleResultOperation):
    def execute(self, *args):
        p = args[0]
        t = args[1]
        r = args[2]
        return p * (1 + r/100)**t
    

class Calculator:
    def __init__(self, operations: list[BaseSingleResultOperation], name="Simple"):
        self.name = name
        self.operations = operations


    def calculate(self, operation_name, *args):
        for operation in self.operations:
            if operation.name == operation_name:
                return operation.execute(*args)
        return None

if __name__ == "__main__":
    simple = Calculator([Addition("add")])
    result = simple.calculate("add", 1,2)
    print(result)

    complex = Calculator([Addition("add"), SimpleIntrest("si"), CompoundIntrest("ci")])
    result = complex.calculate("si", 1000, 2, 5.5)
    print(result)
    result = complex.calculate("add", 1, 2, 3, 4, 5)
    print(result)
    result = complex.calculate("ci", 1000, 2, 5.5)
    print(result)