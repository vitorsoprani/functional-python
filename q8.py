from fundamentals import *

def foo(l: list[int]) -> int:
    if not l:
        return 0

    if l[0] < 0:
        return 1 + foo(tail(l))

    return foo(tail(l))


if __name__ == "__main__":
    print(foo([-0, -10, -30, 10, -5, 1, -5, 1, 5]))
