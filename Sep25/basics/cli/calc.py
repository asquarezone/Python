import sys

def print_usage():
    print("""
usage: calc.py <operation> <arg1> <arg2>
<operation> = add | sub | mul | div
arg1: any number
arg2: any number
          """)

def main(args: list[str]) -> None:
    if args[0] == 'add':
        result = int(args[1]) + int(args[2])
        print(result)

if __name__ == "__main__":
    #print(sys.argv)
    args = sys.argv[1::]
    if len(args) != 3:
        print("Invalid arguments passed")
        print_usage()
        exit(1)
        
    #print(args)
    main(args)
    exit(0)
