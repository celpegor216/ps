def calc(A, B, C):
    if A == B == C:
        return 10000 + A * 1000
    elif A == B and A != C:
        return 1000 + A * 100
    elif A == C and A != B:
        return 1000 + A * 100
    elif B == C and A != B:
        return 1000 + B * 100
    else:
        return max(A, B, C) * 100

N = int(input())
result = 0
for _ in range(N):
    result = max(result, calc(*map(int, input().split())))

print(result)