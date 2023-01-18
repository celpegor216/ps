def solution(s):
    answer = 0
    
    stack = []
    
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    if not stack:
        answer = 1
    
    return answer