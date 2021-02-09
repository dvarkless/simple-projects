def print_fibonacci(input, mode):   # If mode == 1, input is number of iterations,
    n_0 = 0                         # Else - input is the largest desired fibonacci number
    n_1 = 1

    input = max(input, 0)
    print("Fibonacci numbers:")
    if mode is True:
        if input > 0:          # If input == 1, just print  0
            print(n_0)
        else:
            return

        if input > 1:          # If input == 2, print  0, 1 and so on
            print(n_1)
        else:
            return

        for i in range(input - 2):
            n_2 = n_0 + n_1
            print(n_2)

            n_0 = n_1
            n_1 = n_2

    else:
        if input == 0:
            print(n_0)
            return
        if input == 1:
            print(n_1)

        while True:
            n_2 = n_0 + n_1
            if input <= n_2:
                break
            print(n_2)
            n_0 = n_1
            n_1 = n_2
    print("------------------------")


def main():
    print("--------Fibonacci sequence generator--------\n")

    while True:
        print("Type 1 if you want to generate numbers up to certain number")
        print("Type 2 if you want to generate a specific amount of numbers")
        print(">>> ", end='')
        ans = input()
        if ans == "quit" or ans == "q":
            break
        if not ans.isdigit():
            print("You did not enter a number. Try again")
            continue

        if ans == "1":
            print("Type an upper limit of the sequence")
            ans = input()

            if ans == "quit" or ans == "q":
                break
            if not ans.isdigit():
                print("You did not enter a number. Try again")
                continue

            ans = int(ans)
            print_fibonacci(ans, False)

        else:
            print("Type an amount of numbers you want to generate")
            ans = input()

            if ans == "quit" or ans == "q":
                break
                if not ans.isdigit():
                    print("You did not enter a number. Try again")
                    continue

            ans = int(ans)
            print_fibonacci(ans, True)


if __name__ == '__main__':
    main()
