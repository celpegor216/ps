# 이전에 풀었던 '1174 줄어드는 수'와 문제는 동일한데 조건이 다름

N = int(input())

now = [0]

for n in range(N):
    now[-1] += 1

    for m in range(len(now) - 1, 0, -1):
        if now[m - 1] == now[m]:
            now[m - 1] += 1
            
            if m == len(now) - 1:
                now[m] = 0
            else:
                now[m] = now[m + 1] + 1
    
    if now[0] == 10:
        length = len(now)
        now = []
        for n in range(length, -1, -1):
            now.append(n)
    
    if len(now) > 10:
        now = [-1]
        break

for item in now:
    print(item, end='')