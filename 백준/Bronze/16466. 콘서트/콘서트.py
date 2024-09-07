N = int(input())
lst = sorted(map(int, input().split()))

for n in range(N):
    if lst[n] != n + 1:
        print(n + 1)
        break
else:
    print(N + 1)