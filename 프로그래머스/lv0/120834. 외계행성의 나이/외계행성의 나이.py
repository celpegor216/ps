def solution(age):
    answer = ''
    
    while age:
        answer += chr(age % 10 + ord('a'))
        age //= 10
    
    return answer[::-1]