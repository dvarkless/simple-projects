""" 
    This is a solution for karan/Projects
    "Find e to the Nth Digit"

    This script prints euler's number up to
    N'th digit after comma

    Algorithm - sum of the factorials
"""


def print_e(digits):

    try:
        digits = int(digits)
    except:
        print("Error: input must be a number (print_e)")
        return

    digits = max(digits, 0)
    digits = min(digits, 15)

    if digits == 0:         # Limit iterations just to be enought for this precision
        iterations = 3
    elif digits == 1:
        iterations = 5
    elif digits == 2:
        iterations = 6
    elif digits == 3:
        iterations = 8
    else:
        iterations = 50

    e = get_e(iterations)
    e = round(e, digits)
    if digits == 0:
        e = int(e)            # In this case the number will be without comma

    print(e)


def get_e(iterations):
    sum = 0
    for i in range(iterations):
        f = factorial(i)
        sum = sum + 1/f
    return sum


def factorial(number):
    try:

        number = int(number)          # This was added if user wants to call
    except:                           # the function for some other usage
        print("Error: input must be a number (factorial)")
        return

    if number < 0 and number > 40:             # factorial of 40+ is really big number
        print("Error: cannot calculate a factorial of this number")
        return

    sum = 1
    if number == 0:                            # 0! = 1
        return sum
    else:
        for i in range(number, 0, -1):
            sum = sum*i
    return sum


def main():
    print("\n---This program simply prints euler's number---")
    print("type in how many decimal digits you want")
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
        print_e(ans)

        print("type in how many digits do you want")
        print("type (q) to quit")


if __name__ == '__main__':
    main()
