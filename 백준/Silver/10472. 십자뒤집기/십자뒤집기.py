from collections import deque

used = dict()
q = deque()
q.append(('.........', 0))
used.update({'.........': 0})

while q:
    nowb, nowc = q.popleft()

    for i in range(3):
        for j in range(3):
            temp = [list(nowb[x:x+3]) for x in range(0, 7 ,3)]
            for dy, dx in ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = i + dy, j + dx
                if 0 <= ny < 3 and 0 <= nx < 3:
                    if temp[ny][nx] == '.':
                        temp[ny][nx] = '*'
                    else:
                        temp[ny][nx] = '.'
            
            temps = ''.join([''.join(temp[x]) for x in range(3)])
            if temps not in used.keys():
                used[temps] = nowc + 1
                q.append((temps, nowc + 1))

T = int(input())

for t in range(T):
    ans = [list(input()) for _ in range(3)]

    temp = ''.join([''.join(ans[x]) for x in range(3)])
    print(used[temp])