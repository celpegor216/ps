def solution(lottos, win_nums):
    max_result = lottos.count(0)
    min_result = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            max_result += 1
            min_result += 1
    
    result = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    
    return [result[max_result], result[min_result]]