T = int(input())

for t in range(T):
    J, N = map(int, input().split())
    lst = []

    for n in range(N):
        a, b = map(int, input().split())
        lst.append(a * b)

    lst.sort(reverse=True)

    cnt = 0
    total = 0
    while total < J:
        total += lst[cnt]
        cnt += 1
    
    print(cnt)