# 누가 이기고 있는지 기록
# 동점이 되는 순간, 그 전까지 이기고 있던 사람에 시간을 더함
# 동점에서 바뀌는 순간, 누가 이기고 있는지 변경

N = int(input())

a = [0, 0] # 골 수, 이기고 있던 시간
b = [0, 0]
winner = '0'
wintime = 0

for n in range(N):
    team, time = input().split()
    time = int(time[:2]) * 60 + int(time[-2:])

    if team == '1':
        a[0] += 1
    else:
        b[0] += 1
    
    if (team == '1' and a[0] - 1 > b[0]) or (team == '2' and b[0] - 1 > a[0]):
        continue
    elif a[0] > b[0]:
        if winner == '0':
            wintime = time
        winner = '1'
    elif a[0] < b[0]:
        if winner == '0':
            wintime = time
        winner = '2'
    else:
        if winner == '1':
            a[1] += time - wintime
        else:
            b[1] += time - wintime

        winner = '0'

lasttime = 48 * 60
if winner == '1':
    a[1] += lasttime - wintime
elif winner == '2':
    b[1] += lasttime - wintime

print(f'{a[1] // 60:02d}:{a[1] % 60:02d}')
print(f'{b[1] // 60:02d}:{b[1] % 60:02d}')