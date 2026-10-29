from fatorial import fat

def foo(n: int) -> int:
    if n == 0:
        return 1

    return 1/fat(n) + foo(n -1)

if __name__ == "__main__":
    print([foo(x) for x in range(10)])
