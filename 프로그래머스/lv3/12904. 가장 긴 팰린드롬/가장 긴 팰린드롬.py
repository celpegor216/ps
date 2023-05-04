def solution(s):
    answer = 1
    length = len(s)
    
    # 홀수 개수 펠린드롬
    for i in range(1, length - 1):
        temp = 1
        
        while i - temp >= 0 and i + temp < length:
            if s[i - temp] != s[i + temp]:
                break
            temp += 1
        
        answer = max(answer, temp * 2 - 1)
    
    # 짝수 개수 펠린드롬
    for i in range(1, length - 2):
        if s[i] == s[i + 1]:
            temp = 1

            while i - temp >= 0 and i + 1 + temp < length:
                if s[i - temp] != s[i + 1 + temp]:
                    break
                temp += 1

            answer = max(answer, temp * 2)

    return answer