def solution(N, number):
    lst = [[0]]
    
    for i in range(9):
        lst.append([lst[i][0] * 10 + N])
    
    for i in range(2, 9):
        for j in range(1, i):
            for a in lst[j]:
                for b in lst[i - j]:
                    lst[i].append(a + b)
                    if a - b > 0:
                        lst[i].append(a - b)
                    lst[i].append(a * b)
                    if a // b > 0:
                        lst[i].append(a // b)
    
    for i in range(1, 9):
        if number in lst[i]:
            return i

    return -1