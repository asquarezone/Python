from calc import Calculator
from operation import Addition, Subtraction, Division, CircleArea



calc:Calculator|None = None

if __name__ == "__main__":
    calc = Calculator()
    # lets suppport basic operations
    calc.register("add", Addition())
    calc.register("sub", Subtraction())
    calc.register("div", Division())
    result = calc.calculate('add',a=5,b=4)
    print(result)
    calc.register('area', CircleArea())
    result = calc.calculate('area', r = 5)
    print(result)