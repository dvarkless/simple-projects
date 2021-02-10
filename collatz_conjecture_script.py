def calc_steps(input):
    i = 0
    while input > 1:
        if input % 2 == 0:
            input /= 2
        else:
            input = 3*input + 1
        i += 1
    return i


def main():
    print("Collatz Conjecture Algorithm".center(50, "="))

    while True:
        print("Type in the number you want to test".center(50, "="))
        print("q - exit")
        ans = input()
        if ans.isdigit():
            ans = int(ans)
            ans = abs(ans)

            result = calc_steps(ans)

            print("It takes {} steps for the number {} to get to 1".format(
                result, ans))

        if ans == "q":
            break


if __name__ == "__main__":
    main()
