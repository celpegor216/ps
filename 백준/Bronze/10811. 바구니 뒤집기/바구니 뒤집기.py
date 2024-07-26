N, M = map(int, input().split())
lst = [n for n in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    lst = lst[:i] + lst[j:i - 1:-1] + lst[j + 1:]

print(*lst[1:])