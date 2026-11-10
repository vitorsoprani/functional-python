from fundamentals import *

def concat(l1, l2):
    if len(l2) == 1:
        return l1 + l2

    return concat(concat(l1, [head(l2)]), tail(l2))


if __name__ == "__main__":
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(concat(l1, l2))
