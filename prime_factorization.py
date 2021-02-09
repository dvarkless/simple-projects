"""
    This is a solution for karan/Projects
    "Prime Factorization"
    
    This script returns all prime factors of a positive integer

    Algorithm used in get_prime is wheel factorization
    it saves quite a lot of time
"""


def get_prime(number):
    if number % 2 == 0:
        return 2
    if number % 3 == 0:
        return 3
    if number % 5 == 0:
        return 5

    k = 7
    i = 0

    increment = [4, 2, 4, 2, 4, 6, 2, 6]
    # 7, 11, 13, 17, 19, 23, 29, 31, 37...  script assignes k to this values, not all this numbers are primes, but most of them
    while k*k <= number:        # if number is less than k*k, it is 100% prime
        if number % k == 0:
            return k
        k = k + increment[i]
        i = i + 1
        if i > 7:
            i = 0

    return int(number)


def print_all_primes(number):
    print("\n----------------------")
    print(1)

    n = abs(number)

    while n != 1:
        divisor = get_prime(n)
        n = n/get_prime(n)
        if divisor != 1:
            print(divisor)
    print("----------------------\n")


def main():
    print("\n---Prime Factorization program---")
    print("type in any positive integer to find all its prime factors")
    print("type (q) to quit")

    while True:
        print(">>> ", end='')

        ans = input()

        if ans == "q":
            break
        if not ans.isdigit():
            print("Please type an integer")
            continue
        ans = int(ans)
        print_all_primes(ans)

        print("type in any positive integer to find all its prime factors")
        print("type (q) to quit")


if __name__ == '__main__':
    main()
