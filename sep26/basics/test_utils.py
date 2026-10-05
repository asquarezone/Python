from numeric_utils import is_prime, sum_of_multiples_of_3_or_5


def check_prime():
    print(f"is_prime(7) => {is_prime(7)}")
    print(f"is_prime(70) => {is_prime(70)}")
    print(f"is_prime(1) => {is_prime(1)}")

def check_sum_of_multiples():
    print(f"sum_of_multiples_of_3_or_5(1,10) => {sum_of_multiples_of_3_or_5(1,10)}")
    print(f"sum_of_multiples_of_3_or_5(1,1000) => {sum_of_multiples_of_3_or_5(1,1000)}")

if __name__ == "__main__":
    #check_prime()
    #check_sum_of_multiples()
    # calling args by name
    # sum_of_multiples_of_3_or_5(start=1, end=1000)
    # sum_of_multiples_of_3_or_5(end=1000)
    # sum_of_multiples_of_3_or_5(1000)
