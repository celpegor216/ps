N, L = map(int, input().split())
lst = sorted(map(int, input().split()))

for item in lst:
    if item <= L:
        L += 1
    else:
        break

print(L)