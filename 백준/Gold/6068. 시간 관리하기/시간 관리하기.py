N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: (x[1], -x[0]))
start, end = 0, lst[-1][1] - lst[-1][0]

result = -1
while start <= end:
    middle = (start + end) // 2

    now = middle
    flag = 0
    for n in range(N):
        if now + lst[n][0] > lst[n][1]:
            flag = 1
            break
        now += lst[n][0]
    
    if not flag:
        result = middle
        start = middle + 1
    else:
        end = middle - 1

print(result)