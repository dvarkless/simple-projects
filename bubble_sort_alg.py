def bubble_sort(input):
    length = len(input)
    swap_count = 0
    while True:
        for i, val in enumerate(input):
            if i == length-1:
                pass
            elif val > input[i + 1]:
                input[i] = input[i + 1]
                input[i + 1] = val
                swap_count += 1
        if swap_count == 0:
            break
        swap_count = 0

    return input


def main():
    print("Bubble Sort tester program".center(44, "="))
    print("Type \"q\" to stop the program")
    given_list = []
    run = True
    while run:
        print("Type in values you want to sort one-by-one")
        print("Type \"end\" then you finish")
        while True:
            ans = input("Type in another number or \"end\"")
            if not ans.islower():
                if not ans.isupper():
                    try:
                        given_list.append(float(ans))
                    except:
                        print("Error: you can only type in a decimal number")

            if ans == "end":
                break

            if ans == "q":
                run = False
                break

        print(bubble_sort(given_list))
        given_list = []


if __name__ == "__main__":
    main()
