def solution(s):
    answer = 0
    
    for i in range(len(s)):
        stack = []
        flag = 0
        
        for t in s:
            if t in ('(', '{', '['):
                stack.append(t)
            elif stack and ((t == ')' and stack[-1] == '(') or (t == ']' and stack[-1] == '[') or (t == '}' and stack[-1] == '{')):
                    stack.pop()
            else:
                flag = 1
                break
        
        if not flag and not stack:
            answer += 1
        
        s = s[1:] + s[0]
    
    return answer