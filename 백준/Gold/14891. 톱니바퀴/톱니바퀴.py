# 0번의 2 - 1번의 6
# 1번의 2 - 2번의 6
# 2번의 2 - 3번의 6

# 시계 방향으로 회전 > 오른쪽 1칸 이동
# 반시계 방향으로 회전 > 왼쪽 1칸 이동

gears = [input() for _ in range(4)]

K = int(input())

for k in range(K):
    idx, d = map(int, input().split())
    idx -= 1

    move = [0] * 4
    move[idx] = d

    left = idx - 1
    right = idx + 1

    while 0 <= left < 4:
        if gears[left][2] != gears[left + 1][6]:
            move[left] = move[left + 1] * -1
            left -= 1
        else:
            break
    
    while 0 <= right < 4:
        if gears[right][6] != gears[right - 1][2]:
            move[right] = move[right - 1] * -1
            right += 1
        else:
            break
    
    for i in range(4):
        if move[i] == 1:
            gears[i] = gears[i][-1] + gears[i][:-1]
        elif move[i] == -1:
            gears[i] = gears[i][1:] + gears[i][0]
    
result = 0

for i in range(4):
    if gears[i][0] == '1':
        result += 2 ** i

print(result)