'''
Escreva uma função que inverte o conteúdo de uma lista
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

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 6, 7]
    l2 = "vitor"

    print(invert(l1))
    print(invert(l2))



