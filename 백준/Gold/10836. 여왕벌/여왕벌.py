# 해답: https://westmino.tistory.com/43


import sys
input = sys.stdin.readline


N, K = map(int, input().split())

lst = [1] * (N * 2 - 1)
for _ in range(K):
    a, b, c = map(int, input().split())
    for i in range(a, a + b):
        lst[i] += 1
    for i in range(a + b, N * 2 - 1):
        lst[i] += 2

for i in range(N - 1, -1, -1):
    print(lst[i], end=' ')
    print(*lst[N:])