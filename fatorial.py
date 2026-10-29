def fat(n: int) -> int:
    if (n == 0):
        return 1

    return fat(n - 1) * n


if __name__ == "__main__":
    print([fat(x) for x in range(10)])
