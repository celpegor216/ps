N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)] + [[L, -1, -1]]

# 현재 위치, 현재 시각
now = time = 0
for d, r, g in lst:
    time += d - now
    now = d

    # 마지막에 추가한 요소 처리
    if r == g == -1:
        break

    # 빨간불에 들어왔으므로 다음 초록불까지 기다려야 함
    if (time % (r + g)) <= r:
        time += r - (time % (r + g))

print(time)