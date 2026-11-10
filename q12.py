from ehPrimo import ehPrimo

def nPrimos(n: int, i: int, c: int):
    if c == n:
        return

    if ehPrimo(i):
        print(i)
        nPrimos(n, i + 1, c + 1)
        return

    nPrimos(n, i + 1, c)


if __name__ == "__main__":
    nPrimos(int(input()), 1, 0)

