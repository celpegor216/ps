A, B = map(int, input().split())

result = 0

now = 1
now_cnt = 0
total_cnt = 1

while total_cnt <= B:
    if total_cnt >= A:
        result += now

    now_cnt += 1
    if now_cnt == now:
        now += 1
        now_cnt = 0
    
    total_cnt += 1

print(result)