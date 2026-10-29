def head(l: list) -> int:
    return l[0]

def tail(l: list) -> list:
    return l[1:]

def init(l: list) -> list:
    return l[:-1]

def last(l: list) -> int:
    return l[-1]

def len(l: list) -> int:
    if not l:
        return 0

    return 1 + len(tail(l))


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(l)
    print(len(l))
    print(head(l))
    print(tail(l))
    print(init(l))
    print(last(l))

