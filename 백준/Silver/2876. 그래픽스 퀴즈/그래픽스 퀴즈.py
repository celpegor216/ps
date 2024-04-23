# 문제를 다르게 해석함

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

maxc = 0
minv = 6

for i in range(1, 6):
    cnt = 0

    for n in range(N):
        if i in lst[n]:
            cnt += 1
        else:
            cnt = 0
        if maxc < cnt:
            maxc = cnt
            minv = i

print(maxc, minv)