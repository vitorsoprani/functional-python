from fundamentals import *

def nMaiores(l: list[int], n: int) -> int:
    if len(l) == 0:
        return 0

    if head(l) > n:
        return 1 + nMaiores(tail(l), n)

    return nMaiores(tail(l), n)

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(nMaiores(l, 1))
    print(nMaiores(l, 2))
    print(nMaiores(l, 10))

