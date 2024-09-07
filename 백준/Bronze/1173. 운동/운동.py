N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
else:
    time = 0
    X = m
    while N:
        # 운동
        if X + T <= M:
            X += T
            N -= 1
        else:
            X -= R
            if X < m:
                X = m

        time += 1

    print(time)