from intrest import CompoundInterest, SimpleInterest
from emi import MonthlyEMICalculation

if __name__ == "__main__":
    emi = MonthlyEMICalculation()
    print(emi.run({
        "principal": 100000,
        "rate": 7.2,
        "years": 2}))

    si = SimpleInterest()
    print(si.run({
        "principal": 100000,
        "rate": 7.2,
        "years": 2}))

    ci = CompoundInterest()
    print(ci.run({
        "principal": 100000,
        "rate": 7.2,
        "years": 2}))