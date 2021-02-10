"""
    This is a solution for karan/Projects
    "Next Prime Number"
    
    This script gives as many prime numbers
    as requested by user

    Algorithm used in get_prime is wheel factorization
    it saves quite a lot of time
"""


def get_next_prime(input):
    if input == 0:          # This values can't be returned by wheel
        return 1            # so script calculates them "by hand"
    if input == 1:
        return 2
    if input == 2:
        return 3
    if input == 3:
        return 5
    if input == 5:
        return 7

    wheel = [1, 7, 11, 13, 17, 19, 23, 29]
    increment = [6, 4, 2, 4, 2, 4, 6, 2]

    rem = input % 30            # "circumference" of the wheel is 2*3*5 = 30
    i = 0

    while rem not in wheel:     # if input number is not prime
        i = i + 1
        rem = rem + 1
        rem = rem % 30

    input = input + i

    iter = 0
    for iter in range(9):
        if rem == wheel[iter]:
            break

    while True:
        # Here we increase the value at least by one position alongside the wheel
        input = input + increment[iter]

        if is_prime(input) is True:
            break

        iter = iter + 1
        if iter > 7:
            iter = 0

    return int(input)


def is_prime(number):
    if number % 2 == 0:
        return False
    if number % 3 == 0:
        return False
    if number % 5 == 0:
        return False

    k = 7
    i = 0

    increment = [4, 2, 4, 2, 4, 6, 2, 6]

    while k*k <= number:
        if number % k == 0:
            return False
        k = k + increment[i]
        i = i + 1
        if i > 7:
            i = 0

    return True


if __name__ == '__main__':
    print("\n---This program prints as many prime numbers as you want---\n")
    print("----Press R to reset the sequence, press q to quit----")
    print("Type in an amount of numbers you want to see next:")
    count = 0
    last_number = 0

    while True:
        print(">>>", end='')
        ans = input()

        if ans == "q":
            break
        if ans == "r":
            print("-----------------------RESET-----------------------\n")
            count = 0
            last_number = 0
            continue
        if not ans.isdigit():
            print("Please type an integer")
            continue

        ans = int(ans)

        for i in range(ans, 0, -1):
            last_number = get_next_prime(last_number)
            print(last_number)

        count = count + 1
