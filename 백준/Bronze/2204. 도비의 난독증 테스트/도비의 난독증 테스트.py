while 1:
    N = int(input())

    if N == 0:
        break

    lst = []

    for n in range(N):
        S = input()
        lst.append((S.upper(), S))

    print(sorted(lst)[0][1])