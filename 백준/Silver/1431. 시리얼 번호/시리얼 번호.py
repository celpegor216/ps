N = int(input())
lst = []

for _ in range(N):
    S = list(input())

    total = 0
    for i in range(len(S)):
        if S[i].isdigit():
            S[i] = int(S[i])
            total += int(S[i])
        else:
            S[i] = ord(S[i])

    lst.append((len(S), total, S))

lst.sort()

for line in lst:
    for item in line[-1]:
        if 0 <= item < 10:
            print(item, end='')
        else:
            print(chr(item), end='')
    print()