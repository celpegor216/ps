import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    result[a] += 1
    result[b] += 1

for n in range(1, N + 1):
    print(result[n])