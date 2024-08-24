lst = list(range(21))

N = 10
for _ in range(N):
    A, B = map(int, input().split())
    lst[A:B + 1] = lst[B:A - 1:-1]

print(*lst[1:])