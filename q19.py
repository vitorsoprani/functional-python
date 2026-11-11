'''
Escreva uma função que receba uma palavra e gere seu palíndromo
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


def invert(l):
    if not l:
        return []

    return concat(invert(tail(l)), [head(l)])

def palindromo(l1):
    return concat(list(l1), invert(l1))

if __name__ == "__main__":
    l1 = "vitor"
    print(palindromo(l1))


