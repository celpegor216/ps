def solution(rows, columns, queries):
    answer = []
    
    lst = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        up, left, down, right = [x - 1 for x in query]
        
        min_v = 21e8
        for i in range(up, down + 1):
            if i == up or i == down:
                for j in range(left, right + 1):
                    if min_v > lst[i][j]:
                        min_v = lst[i][j]
            else:
                 if min_v > lst[i][left]:
                    min_v = lst[i][left]
                
                 if min_v > lst[i][right]:
                    min_v = lst[i][right]
        
        temp = lst[up][right]
        for i in range(right, left, -1):
            lst[up][i] = lst[up][i - 1]
        lst[up][left] = lst[up + 1][left]
        
        temp2 = lst[down][right]
        for i in range(down, up + 1, -1):
            lst[i][right] = lst[i - 1][right]
        lst[up + 1][right] = temp
        
        temp = lst[down][left]
        for i in range(left, right):
            lst[down][i] = lst[down][i + 1]
        lst[down][right - 1] = temp2
        
        temp2 = lst[up][left]
        for i in range(up, down):
            lst[i][left] = lst[i + 1][left]
        lst[down - 1][left] = temp
        
        answer.append(min_v)
    
    return answer