# 해답: https://school.programmers.co.kr/questions/24730

def solution(n, k):
    answer = []
    
    # 팩토리얼 값 저장
    facts = [1]
    
    for i in range(1, n + 1):
        facts.append(facts[i - 1] * i)
    
    numbers = [i for i in range(1, n + 1)]
    
    while n:
        answer.append(numbers.pop((k - 1) // facts[n - 1]))
        k %= facts[n - 1]
        n -= 1
        
    return answer