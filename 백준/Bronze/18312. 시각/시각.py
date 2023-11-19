N, K = map(int, input().split())

hour = 0
min = 0
sec = 0

result = 0

while 1:
    s = f'{hour:02d}{min:02d}{sec:02d}'

    if str(K) in s:
        result += 1
    
    if hour == N and min == 59 and sec == 59:
        break

    sec += 1

    if sec == 60:
        sec = 0
        min += 1
    
    if min == 60:
        min = 0
        hour += 1

print(result)