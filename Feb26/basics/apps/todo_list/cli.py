import argparse

# parser
parser = argparse.ArgumentParser(
    description="My Program"
)
parser.add_argument("-n","--name", help="Name of the user")
# boolean arguments
parser.add_argument("-v", "--verbose", action="store_true",help="Enable verbose mode")
parser.add_argument("-c", "--count", type=int, default=0, help="Count Value")
args = parser.parse_args()

print(args.name)
print(args.verbose)
print(args.count)
