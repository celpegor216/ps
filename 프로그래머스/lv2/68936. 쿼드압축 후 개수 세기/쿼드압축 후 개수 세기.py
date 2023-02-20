def solution(arr):
    answer = [0, 0]
    
    def func(length, y, x):
        nonlocal answer
        
        if length == 1:
            answer[arr[y][x]] += 1
            return
        
        flag = 0
        for i in range(length):
            if not flag:
                for j in range(length):
                    if arr[y + i][x + j] != arr[y][x]:
                        flag = 1
                        break
        
        if not flag:
            answer[arr[y][x]] += 1
        else:
            half = length // 2
            for i in range(2):
                for j in range(2):
                    func(half, y + i * half, x + j * half)
    
    func(len(arr), 0, 0)
    
    return answer