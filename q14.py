from fundamentals import head, tail, len

def has(l: list[int], n: int) -> bool:
    if len(l) == 0:
        return False

    if head(l) == n:
        return True

    return has(tail(l), n)


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    print(has(l, 3))
    print(has(l, 8))

