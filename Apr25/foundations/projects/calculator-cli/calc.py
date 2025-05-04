import argparse
from calc.core.investment import SIPCalculator, LumpsumInvestmentCalculator


def create_argument_parser() -> argparse.ArgumentParser:
    """This method creates argument parser
    """
    parser = argparse.ArgumentParser(
        prog='calc',
        description='This program performs differnt types of calculations like sip, lumpsum',
    )
    parser.add_argument("-t", "--type",type=str,choices=['sip','lumpsum'],default='sip', help="Type of calculator")
    parser.add_argument("-p", "--principal", type=float,help="Investment Amount")
    parser.add_argument("-d", "--duration", type=int,  help="investment duration in months")
    parser.add_argument("-r","--rate", type=float, help="investment return rate")
    return parser
    


if __name__ == "__main__":
    parser = create_argument_parser()
    args = parser.parse_args()
    p = args.principal
    t = args.duration
    r = args.rate
    calc_type = args.type
    calculator = None
    if args.type == "sip":
        calculator = SIPCalculator(p,r,t)
    elif args.type == "lumpsum":
        calculator = LumpsumInvestmentCalculator(p,r,t)
    result = round(calculator.calculate(),2)
    print(f"The future value of {p} after {args.type} is {result}")



