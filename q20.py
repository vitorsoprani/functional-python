'''
Defina a função strip que dadas duas listas, retira da segunda todos os elementos que
ocorrem na primeira, em qualquer quantidade
'''

def head(l):
    return l[0]

def tail(l):
    return l[1:]

def length(l):
    if not l:
        return 0

    return 1 + length(tail(l))

def concat(l1, l2):
    if length(l1) == 0:
        return l2
    if length(l2) <= 1:
        return l1 + l2

    return concat(concat(l1, [head(l2)]), tail(l2))

def has(l, n):
    if length(l) == 0:
        return False

    if head(l) == n:
        return True

    return has(tail(l), n)

def strip(l1, l2):
    if length(l2) == 0:
        return []

    if has(l1, head(l2)):
        return strip(l1, tail(l2))

    return concat([head(l2)], strip(l1, tail(l2)))


if __name__ == "__main__":
    l1 = [1, 2, 7, 8]
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(strip(l1, l2))
