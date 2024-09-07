N, M = map(int, input().split())
lst = [n for n in range(N)]

for _ in range(M):
    i, j, k = map(lambda x: int(x) - 1, input().split())
    lst[i:j + 1] = lst[k:j + 1] + lst[i:k]

print(*[item + 1 for item in lst])