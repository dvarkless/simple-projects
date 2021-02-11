def merge_sort(input):
    if input == []:
        return input
    length = len(input)
    if length != 1:
        list_1 = input[:length//2]
        list_2 = input[length//2:]

        list_1 = merge_sort(list_1)
        list_2 = merge_sort(list_2)
    else:
        return input

    result = []

    while len(list_1) != 0 or len(list_2) != 0:
        if len(list_1) == 0:
            result.append(list_2[0])
            del list_2[0]
        elif len(list_2) == 0:
            result.append(list_1[0])
            del list_1[0]

        elif list_1[0] <= list_2[0]:
            result.append(list_1[0])
            del list_1[0]
        else:
            result.append(list_2[0])
            del list_2[0]
    return result


def main():
    print("Merge Sort tester program".center(44, "="))
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

        print(merge_sort(given_list))
        given_list = []


if __name__ == "__main__":
    main()
