N, B, H, W = map(int, input().split())

result = B + 1

for _ in range(H):
    cost = int(input())
    lst = list(map(int, input().split()))

    for item in lst:
        if item >= N:
            result = min(result, N * cost)
            break

print('stay home' if result > B else result)