"""
    This is a solution for karan/Projects
    "Find PI to the Nth Digit"
    
    This script returns Pi up to 15-th decimal number
"""


def get_pi(iterations):
    """
        This function prints Pi
        using the Brent-Salamin's algorithm

    """

    a_n = 1                                        # Starting constants
    b_n = 0.70710678118654752440084436210485       # 1 / root(2)
    t_n = 0.25
    p_n = 1

    a_prev = a_n
    b_prev = b_n
    t_prev = t_n
    p_prev = p_n

    iterations = max(iterations, 1)
    iterations = min(iterations, 100)

    for i in range(iterations):
        a_prev = a_n
        b_prev = b_n
        t_prev = t_n
        p_prev = p_n

        a_n = (a_prev + b_prev)/2
        b_n = (a_prev * b_prev)**0.5
        t_n = t_prev - p_prev*(a_prev - a_n)**2
        p_n = 2*p_prev

    ans = (a_n + b_n)**2
    ans = ans / (4*t_n)

    return ans


def print_pi(digit):

    digit = max(digit, 0)
    digit = min(digit, 15)
    if digit < 3:               # This was added because we don't need so much
        iterations = 1          # precision to print routhly-rounded Pi
    elif digit < 8:
        iterations = 2
    else:
        iterations = 4

    pi = get_pi(iterations)
    if digit == 0:
        pi = int(pi)
    else:
        pi = round(pi, digit)

    print(pi)


def main():
    print("\n---This program simply prints pi---")
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
        print_pi(ans)

        print("type in how many digits do you want")
        print("type (q) to quit")


if __name__ == '__main__':
    main()
