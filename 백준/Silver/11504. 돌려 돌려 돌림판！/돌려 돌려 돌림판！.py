T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    X = int(''.join(input().split()))
    Y = int(''.join(input().split()))
    lst = list(map(int, input().split()))

    result = 0
    for i in range(N):
        now = 0
        for j in range(M):
            now = now * 10 + lst[(i + j) % N]
        if X <= now <= Y:
            result += 1

    print(result)