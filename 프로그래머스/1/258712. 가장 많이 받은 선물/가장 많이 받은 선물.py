def solution(friends, gifts):
    N = len(friends)

    name_to_idx = dict()
    for n in range(N):
        name_to_idx[friends[n]] = n
        
    lst = [[0] * N for _ in range(N)]
    total = [0] * N
    
    for gift in gifts:
        A, B = gift.split()
        a, b = name_to_idx[A], name_to_idx[B]
        lst[a][b] += 1
        total[a] += 1
        total[b] -= 1
    
    result = [0] * N
    
    for i in range(N):
        for j in range(i + 1, N):                
            if lst[i][j] < lst[j][i]:
                result[j] += 1
            elif lst[i][j] > lst[j][i]:
                result[i] += 1
            else:
                if total[i] < total[j]:
                    result[j] += 1
                elif total[i] > total[j]:
                    result[i] += 1
    
    return max(result)