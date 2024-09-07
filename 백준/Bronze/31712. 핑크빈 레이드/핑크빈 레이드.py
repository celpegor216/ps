N = 3
lst = [list(map(int, input().split())) for _ in range(N)]
H = int(input())

time = 0
while 1:
    for c, d in lst:
        if not time % c:
            H -= d
    
    if H <= 0:
        print(time)
        break

    time += 1