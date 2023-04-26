# 이분 탐색까진 생각해서 구현했는데 그래도 효율성 하나도 통과 못 함
# 틀린 부분 찾았다,,, end랑 start 갱신할 때 그냥 -1 +1을 했네

def solution(stones, k):
    answer = 0
    
    lst = sorted(set(stones))
    
    start, end = 0, len(lst) - 1
    
    while start <= end:
        middle = (start + end) // 2
        
        now = lst[middle]
        check = 0
        flag = 0
        
        for stone in stones:
            if stone < now:
                check += 1
                
                if check == k:
                    flag = 1
                    break
            else:
                check = 0
        
        if flag:
            end = middle - 1
        else:
            answer = now
            start = middle + 1
    
    return answer