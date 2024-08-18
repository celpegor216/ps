T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    result = 0
    maxv = 0
    for n in range(N - 1, -1, -1):
        if maxv < lst[n]:
            maxv = lst[n]
        else:
            result += maxv - lst[n]
    
    print(result)