import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
lst.sort()

result_cnt = 0
result_v = now_v = lst[0] - 1
now_cnt = 0

for i in range(N):
    if lst[i] != now_v:
        if now_cnt > result_cnt:
            result_cnt = now_cnt
            result_v = now_v
        now_cnt = 1
        now_v = lst[i]
    else:
        now_cnt += 1

if now_cnt > result_cnt:
    result_cnt = now_cnt
    result_v = now_v

print(result_v)