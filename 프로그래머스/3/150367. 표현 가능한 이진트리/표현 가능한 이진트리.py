from collections import deque

def solution(numbers):
    answer = []
    
    sizes = [1]
    
    for n in range(10):
        sizes.append(sizes[n] + (2 ** (n + 1)))
    
    for number in numbers:
        if number == 1:
            answer.append(1)
            continue
        
        tmp = bin(number)[2:]
        length = len(tmp)
        half = 0
        
        for i in range(10):
            if sizes[i] < length <= sizes[i + 1]:
                tmp = '0' * (sizes[i + 1] - length) + tmp
                length = sizes[i + 1]
                half = i
                break
        
        used = [0] * length
        
        if tmp[length // 2] == '1':        
            q = deque()
            q.append((length // 2, half))
            used[length // 2] = 1
            
            while q:
                now, width = q.popleft()
                
                if width < 0:
                    continue
                
                left = now - (2 ** width)
                if not used[left] and 0 <= left and tmp[left] == '1':
                    q.append((left, width - 1))
                    used[left] = 1
                
                right = now + (2 ** width)
                if not used[right] and right < length and tmp[right] == '1':
                    q.append((right, width - 1))
                    used[right] = 1
        
        flag = 1
        for i in range(length):
            if (tmp[i] == '1' and used[i] == 1) or (tmp[i] == '0' and used[i] == 0):
                continue
            else:
                flag = 0
                break
        
        answer.append(flag)
    
    return answer