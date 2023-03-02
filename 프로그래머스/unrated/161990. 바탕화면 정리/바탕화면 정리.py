def solution(wallpaper):
    answer = [21e8, 21e8, 0, 0] # 좌 상 우 하
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < answer[0]:
                    answer[0] = i
                if i > answer[2]:
                    answer[2] = i
                
                if j < answer[1]:
                    answer[1] = j
                if j > answer[3]:
                    answer[3] = j
    
    answer[-1] += 1
    answer[-2] += 1
    
    return answer