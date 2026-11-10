
def ehPrimo(n: int) -> bool:
    def _nDiv(n: int, i: int) -> int:
        if i == 1:
            return 1

        if (n % i) == 0:
            return 1 + _nDiv(n, i - 1)
        else:
            return _nDiv(n, i - 1)

    return _nDiv(n, n) == 2

if __name__ == "__main__":
    n = int(input())

    print(ehPrimo(n))

