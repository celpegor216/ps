import sys
input = sys.stdin.readline

result = 0
try:
    N, K = map(int, input().strip().split())

    A = B = 0

    for _ in range(N):
        a, b = map(float, input().strip().split())

        if result:
            continue

        OP = A + a * 1.5
        A += a
        B += b

        if A >= K or A >= B + 50 or (OP >= K and B < K) or (OP >= B + 50):
            result = 1
        elif A < K and B >= K:
            result = -1
except:
    pass
finally:
    print(result)