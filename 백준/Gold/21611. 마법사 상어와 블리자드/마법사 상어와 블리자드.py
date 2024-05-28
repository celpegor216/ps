N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
lst = [0] * N ** 2

length = N
y = 0
x = -1
idx = 0
d = 1

while length:
    for i in range(length):
        x += d
        lst[idx] = board[y][x]
        idx += 1
    
    length -= 1
    
    for i in range(length):
        y += d
        lst[idx] = board[y][x]
        idx += 1
    
    d *= -1

lst.reverse()

directions = [0, 4, 2, 1, 3]

result = [0] * 4

for _ in range(M):
    # 마법 시전
    D, S = map(int, input().split())    # 위/아래/왼쪽/오른쪽
    D = directions[D]

    base = 0
    for s in range(S):
        lst[base + 2 * (s + 1) * D - 1] = 0
        base += 8 * (s + 1) - 1
    
    # 구슬 폭발
    stack = [[0, 1]]
    for i in range(1, N ** 2):
        if not lst[i]:
            continue
        
        if stack[-1][0] != lst[i]:
            stack.append([lst[i], 1])
        else:
            stack[-1][1] += 1
        
    while 1:
        flag = 0

        new_stack = []

        for item in stack:
            if item[0] == 0:
                new_stack.append(item)
            elif item[1] > 3:
                result[item[0]] += item[1]
                flag = 1
            elif item[0] == new_stack[-1][0]:
                new_stack[-1][1] += item[1]
            else:
                new_stack.append(item)

        stack = new_stack

        if not flag:
            break                    
    
    # 구슬 변화
    new_lst = [0]
    for item in stack[1:]:
        new_lst += item[::-1]

    lst = new_lst + [0] * (N ** 2 - len(new_lst))

print(result[1] + result[2] * 2 + result[3] * 3)