N, L = map(int, input().split())

maxv = 0    # 가장 많은 검은 줄
maxc = 0    # 가장 많은 검은 줄을 가지고 있는 얼룩말의 수

for _ in range(N):
    S = input().split('0')
    cnt = 0
    for item in S:
        if item:
            cnt += 1
    if cnt > maxv:
        maxv = cnt
        maxc = 1
    elif cnt == maxv:
        maxc += 1

print(maxv, maxc)