def solution(p):
    def check(w):
        stack = []
        flag = 1
        
        for i in range(len(w)):
            if w[i] == '(':
                stack.append('(')
            else:
                if not stack or stack[-1] == ')':
                    flag = 0
                    break
                else:
                    stack.pop()
        
        return flag
    
    def divide(w):
        # 1. 빈 문자열인지 확인
        if len(w) == 0:
            return ''
        
        # 2. 균형잡힌 괄호 문자열로 분리
        cnt_l = 0
        cnt_r = 0
        idx = 0
        
        for i in range(len(w)):
            if w[i] == '(':
                cnt_l += 1
            else:
                cnt_r += 1
            
            if cnt_l == cnt_r:
                idx = i
                break
        
        # 올바른 문자열인지 확인
        if check(w[:idx + 1]):
            return w[:idx + 1] + divide(w[idx + 1:])
        else:
            temp = ''
            
            for i in range(1, idx):
                if w[i] == '(':
                    temp += ')'
                else:
                    temp += '('
            
            return '(' + divide(w[idx + 1:]) + ')' + temp
    
    return divide(p)