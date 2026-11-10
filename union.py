from fundamentals import *

def has(l: list[int], n: int) -> bool:
    if len(l) == 0:
        return False

    if head(l) == n:
        return True

    return has(tail(l), n)


def concat(l1, l2):
    if len(l2) == 1:
        return l1 + l2

    return concat(concat(l1, [head(l2)]), tail(l2))

def union(l1, l2):
    if len(l2) == 1:
        if has(l1, head(l2)):
            return l1

        return concat(l1, l2)

    return union(union(l1, [head(l2)]), tail(l2))


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3, 4, 5, 6]

    print(concat(l1, l2))
    print(union(l1, l2))

