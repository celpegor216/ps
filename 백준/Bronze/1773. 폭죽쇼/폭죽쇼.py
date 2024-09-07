N, C = map(int, input().split())

checks = [0] * (C + 1)
for _ in range(N):
    A = int(input())
    for i in range(A, C + 1, A):
        checks[i] += 1

print(C - checks.count(0) + 1)