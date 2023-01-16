def solution(answers):
    lst = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    max_cnt = [0, 0, 0]
    
    for i in range(3):
        idx = 0
        for a in answers:
            if lst[i][idx] == a:
                max_cnt[i] += 1
            idx += 1
            if idx == len(lst[i]):
                idx = 0 
    
    print(max_cnt)
    
    max_lst = []
    max_v = 0
    
    for i in range(3):
        if max_cnt[i] > max_v:
            max_lst = [i + 1]
            max_v = max_cnt[i]
        elif max_cnt[i] == max_v:
            max_lst.append(i + 1)
    
    return max_lst