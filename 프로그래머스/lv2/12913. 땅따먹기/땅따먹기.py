# 해답: https://latte-is-horse.tistory.com/229

def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i - 1][x] for x in range(4) if x != j])
    
    answer = max(land[-1])
    
    return answer