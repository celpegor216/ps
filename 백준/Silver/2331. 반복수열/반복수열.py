A, P = map(int, input().split())
lst = [A]

while 1:
    before = lst[-1]
    nxt = 0
    while before:
        nxt += (before % 10) ** P
        before //= 10
    if nxt in lst:
        print(lst.index(nxt))
        break
    lst.append(nxt)