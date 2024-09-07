N = int(input())
# 제출 시각 t, 점수 s
lst = [list(map(int, input().split())) for _ in range(N)]

max_s = 0
min_t = 21e8
result_idx = -1
for i in range(N):
    t, s = lst[i]
    if max_s < s:
        max_s = s
        min_t = t
        result_idx = i
    elif max_s == s and min_t > t:
        min_t = t
        result_idx = i

if max_s == 0:
    print(0)
else:
    print(min_t + result_idx * 20)