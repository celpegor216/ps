coins = float(input()) // 0.99
N = int(input())
lst = list(map(int, input().split()))

if coins >= 2:
    coins = 2

result_days = 0
result_maxv = 0

start = 0
cnt = 0
used = [0] * 25

for end in range(N):
    used[lst[end]] += 1
    
    if not lst[end]:
        cnt += 1
        
        while cnt > coins:
            used[lst[start]] -= 1
            if not lst[start]:
                cnt -= 1
            start += 1

    days = sum(used)

    if result_days < days:
        result_days = days
    
    result_maxv = max(result_maxv, lst[end])

print(result_days)
print(result_maxv)