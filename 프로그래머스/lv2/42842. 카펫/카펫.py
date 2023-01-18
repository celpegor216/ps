# 갈색 가로 = 노랑 가로 + 2
# 갈색 세로 = 노랑 세로
# 갈색 갯수 = (노랑 가로 + 노랑 세로 + 3) * 2
# 노랑 가로 > 노랑 세로
# 노랑 세로 = 노랑 갯수 / 노랑 가로

def solution(brown, yellow):
    answer = []
    
    for row in range(1, yellow + 1):
        if not yellow % row:
            col = yellow // row
            if (row + col) * 2 + 4 == brown:
                answer = [col + 2, row + 2]
                break
    
    return answer