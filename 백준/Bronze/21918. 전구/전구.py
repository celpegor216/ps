N, M = map(int, input().split())
lst = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    b -= 1

    if a == 1:
        lst[b] = c
    elif a == 2:
        for i in range(b, c):
            lst[i] = 1 if not lst[i] else 0
    elif a == 3:
        for i in range(b, c):
            lst[i] = 0
    elif a == 4:
        for i in range(b, c):
            lst[i] = 1

print(*lst)