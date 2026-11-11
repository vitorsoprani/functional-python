'''
Defina a função consoantList que recebe dois parâmetros: o primeiro é uma string
que contém apenas consoantes, e o segundo é uma string “livre”. A função retorna
verdadeiro se somente se todas as consoantes da segunda lista, incluindo
repetições, ocorrem na primeira lista, na mesma ordem.
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

def equals(l1, l2):
    if length(l1) == 0 and length(l2) == 0:
        return True
    if length(l1) == 0:
        return False
    if length(l2) == 0:
        return False

    if head(l1) == head(l2):
        return equals(tail(l1), tail(l2))

    return False

def consoantList(consoants, word):
    return(equals(consoants, strip("aeiou", word)))

if __name__ == "__main__":
    l1 = "sdd"
    l2 = "saudade"
    l3 = "saude"
    print(consoantList(l1, l2))
    print(consoantList(l1, l3))
