def get_primes(max_val):
    numbers = list(range(max_val+1))
    numbers[1] = 0
    prime = 2
    iter = prime

    while prime*prime <= max_val:
        while prime*iter <= max_val:
            numbers[prime*iter] = 0
            if prime == 2:
                iter += 1
            else:
                iter += 2

        for x in range(prime+1, max_val):
            if numbers[x] != 0:
                prime = x
                iter = prime
                break

    while True:
        try:
            numbers.remove(0)
        except:
            break
    return numbers


def main():
    print("\n---Sieve of Eratosthenes algorithm---")
    print("type in any natural number to find all prime numbers before it")
    print("type \'q\' to quit")

    while True:
        print(">>> ", end='')

        ans = input()

        if ans == "q":
            break
        if not ans.isdigit():
            print("Please type an integer")
            continue
        ans = int(ans)
        primes = get_primes(ans)

        for x in range(len(primes)):
            print(primes[x])

        print("type in any natural number to find all prime numbers before it")
        print("type (q) to quit")


if __name__ == '__main__':
    main()
