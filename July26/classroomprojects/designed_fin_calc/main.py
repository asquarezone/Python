from intrest import CompoundInterest, SimpleInterest
from emi import MonthlyEMICalculation
from registry import REGISTER



if __name__ == "__main__":
    
    # emi = MonthlyEMICalculation()
    # print(emi.run({
    #     "principal": 100000,
    #     "rate": 7.2,
    #     "years": 2}))

    # si = SimpleInterest()
    # print(si.run({
    #     "principal": 100000,
    #     "rate": 7.2,
    #     "years": 2}))

    # ci = CompoundInterest()
    # print(ci.run({
    #     "principal": 100000,
    #     "rate": 7.2,
    #     "years": 2}))
    operations:dict = {}
    for name, value in REGISTER.items():
        print(f"{name} => {value}")
        operations[name] = value()
        print(operations[name].run(
            {
        "principal": 100000,
        "rate": 7.2,
        "years": 2}))
    


