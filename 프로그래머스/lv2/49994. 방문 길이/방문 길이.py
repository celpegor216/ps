def solution(dirs):
    answer = 0
    
    used = [[[] for _ in range(11)] for _ in range(11)]
    
    y, x = 5, 5
    
    for d in dirs:
        if d == 'U':
            if 0 <= y - 1 < 11 and 0 <= x < 11:
                if 3 not in used[y - 1][x] and 1 not in used[y][x]:
                    used[y - 1][x].append(3)
                    used[y][x].append(1)
                    answer += 1
                y -= 1
        elif d == 'D':
            if 0 <= y + 1 < 11 and 0 <= x < 11:
                if 1 not in used[y + 1][x] and 3 not in used[y][x]:
                    used[y + 1][x].append(1)
                    used[y][x].append(3)
                    answer += 1
                y += 1
        elif d == 'L':
            if 0 <= y < 11 and 0 <= x - 1 < 11:
                if 4 not in used[y][x - 1] and 2 not in used[y][x]:
                    used[y][x - 1].append(4)
                    used[y][x].append(2)
                    answer += 1
                x -= 1
        elif d == 'R':
            if 0 <= y < 11 and 0 <= x + 1 < 11:
                if 2 not in used[y][x + 1] and 4 not in used[y][x]:
                    used[y][x + 1].append(2)
                    used[y][x].append(4)
                    answer += 1
                x += 1 
    
    return answer