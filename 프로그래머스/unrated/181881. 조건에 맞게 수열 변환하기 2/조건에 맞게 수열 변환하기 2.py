def solution(arr):
    answer = 0
    
    while 1:
        temp = []
        
        for item in arr:
            if item >= 50 and not item % 2:
                temp.append(item // 2)
            elif item < 50 and item % 2:
                temp.append(item * 2 + 1)
            else:
                temp.append(item)
        
        if temp == arr:
            return answer
    
        arr = temp[:]
        answer += 1