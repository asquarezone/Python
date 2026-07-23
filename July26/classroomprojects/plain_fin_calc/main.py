"""
This module will be the entry point of plain fin calc
"""

import argparse
from calc import simple_intrest, compound_interest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Plain Finance Calculator")
    parser.add_argument('--principal', type=float, help='Credit principal', required=True)
    parser.add_argument('--periods', type=int, help='Number of years', default=5)
    parser.add_argument('--interest', type=float, help='Credit interest per annum',default=12)
    parser.add_argument('--type', type=str, help='Type of payment', choices=['simple', 'compound'], default='compound')
    return parser
def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.type == 'simple':
        print(f'Simple Interest = {simple_intrest(args.principal, args.periods, args.interest)}')
    else:
        print(f'Compound Interest = {compound_interest(args.principal, args.periods, args.interest)}')


if __name__ == "__main__":
    main()