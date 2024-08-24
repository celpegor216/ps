N = int(input())
result = 0

for _ in range(N):
    A, D, G = map(int, input().split())

    res = A * (D + G)
    if A == D + G:
        res *= 2
    
    result = max(result, res)

print(result)