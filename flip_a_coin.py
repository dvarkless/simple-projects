import random as r


def flip():
    return r.randint(0, 1)


def calc_flips(i):
    tails = 0
    heads = 0
    for x in range(i):
        if flip() == 0:
            tails += 1
        else:
            heads += 1

    return heads, tails


def main():
    print("Coin flipping simulator".center(44, "="))
    print("Type in how many times you want to flip a coin")
    while True:
        ans = input()
        if ans.isdigit():
            ans = int(ans)
            ans = abs(ans)

            coin = calc_flips(ans)
            if ans == 0:
                if coin[0] == 0:
                    print("It's a tail!")
                else:
                    print("It's a head!")
            else:
                print("There are {} heads and {} tails".format(
                    coin[1], coin[0]))

        if ans == "q":
            break


if __name__ == "__main__":
    main()
