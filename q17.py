'''
Defina uma função que dada uma lista de inteiros e um número n, retorne outra lista
contendo apenas de elementos de valor superior a n
'''

def head(l: list[int]) -> int:
    return l[0]

def tail(l: list[int]) -> list[int]:
    return l[1:]

def length(l: list) -> int:
    if not l:
        return 0

    return 1 + length(tail(l))

def concat(l1, l2):
    if length(l1) == 0:
        return l2

    if length(l2) == 0:
        return l1

    if length(l2) == 1:
        return l1 + l2

    return concat(concat(l1, [head(l2)]), tail(l2))

def maiores(l: list[int], n: int) -> list[int]:
    if length(l) == 0:
        return []

    if head(l) > n:
        return concat([head(l)],maiores(tail(l), n))

    return maiores(tail(l), n)

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(maiores(l, 1))
    print(maiores(l, 7))
    print(maiores(l, 9))
    print(maiores(l, 10))
