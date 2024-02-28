T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    now = 0
    result = -21e8

    for n in range(N):
        if now + lst[n] > lst[n]:
            now += lst[n]
        else:
            now = lst[n]
        result = max(result, now)
    
    print(result)