# 시간초과 해결 힌트: https://velog.io/@sugenius77/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%97%B0%EC%86%8D-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%95%A9%EC%9D%98-%EA%B0%9C%EC%88%98

def solution(elements):
    nums = set()
    
    total = sum(elements)
    length = len(elements)
    
    for i in range(1, (length // 2) + 1):
        temp = sum(elements[:i])
        start = 0
        end = i
        
        for j in range(length):            
            nums.add(temp)
            nums.add(total - temp)
            temp -= elements[start]
            temp += elements[end]
            start += 1
            end += 1
            if end == length:
                end = 0
            
    nums.add(total)
    
    return len(nums)