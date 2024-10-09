TC = int(input())

for _ in range(TC):
    idx, S = input().split()
    idx = int(idx) - 1
    for i in range(len(S)):
        if i == idx:
            continue
        print(S[i], end='')
    print()