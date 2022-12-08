# [1, 2, 3, 2, 3, 4, 5, 2]

def solution(prices):
    answer = [x for x in range(len(prices) - 1, -1, -1)]
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer[i] -= len(prices) - 1 - j
                break
    
    return answer