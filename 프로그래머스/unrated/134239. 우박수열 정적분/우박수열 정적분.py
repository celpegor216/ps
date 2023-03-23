def solution(k, ranges):
    # 우박수열 구하기
    lst = [k]
    
    while k > 1:
        if not k % 2:
            k //= 2
        else:
            k = k * 3 + 1
        lst.append(k)
        
    # 정적분값 구하기
    sums = []
    length = len(lst)
    
    for i in range(length - 1):
        sums.append((lst[i] + lst[i + 1]) * 0.5)
    
    # 구간 합 구하기
    answer = []
    
    for r in ranges:
        if r[0] > length - 1 + r[1] or not 0 <= r[0] < length or not -length < r[1] <= 0:
            answer.append(-1)
        elif r[0] == r[1] == 0:
            answer.append(sum(sums))
        else:
            answer.append(sum(sums[r[0]:length - 1 + r[1]]))
    
    return answer