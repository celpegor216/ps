N, M = map(int, input().split())
lst = []

for m in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    lst.append((a, m + 1))
    lst.append((b, m + 1))

lst.sort()

N -= 1
N %= (M * 2)

print(lst[N][1])