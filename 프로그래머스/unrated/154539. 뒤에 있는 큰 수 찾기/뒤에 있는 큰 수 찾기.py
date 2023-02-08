# 해답: https://velog.io/@wlals425315/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-154539-%EB%92%A4%EC%97%90-%EC%9E%88%EB%8A%94-%ED%81%B0-%EC%88%98-%EC%B0%BE%EA%B8%B0

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer