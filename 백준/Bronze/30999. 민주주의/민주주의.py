N, M = map(int, input().split())

result = 0
for _ in range(N):
    S = input()
    result += 1 if S.count('O') > M // 2 else 0

print(result)