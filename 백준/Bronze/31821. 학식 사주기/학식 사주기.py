N = int(input())
lst = [int(input()) for _ in range(N)]

M = int(input())
result = 0
for _ in range(M):
    result += lst[int(input()) - 1]

print(result)