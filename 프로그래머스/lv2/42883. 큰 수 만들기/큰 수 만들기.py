# 해답: https://velog.io/@injoon2019/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0

def solution(number, k):
    stack = []
    cnt = k
    
    for num in number:
        while cnt and stack and stack[-1] < num:
            stack.pop()
            cnt -= 1
        stack.append(num)
    
    return ''.join(stack) if not cnt else ''.join(stack[:-cnt])