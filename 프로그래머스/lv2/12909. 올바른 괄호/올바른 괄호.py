def solution(s):
    stack = []
    flag = 0
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = 1
                break
    
    if not flag and not stack:
        return True
    else:
        return False