while 1:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    dic = dict()

    for n in range(N):
        tmp = list(map(int, input().split()))

        for item in tmp:
            if dic.get(item):
                dic[item] += 1
            else:
                dic[item] = 1
    
    lst = list(dic.items())
    lst.sort(key=lambda x: (-x[1], x[0]))

    second = lst[1][1]
    result = []

    for item in lst:
        if item[1] == second:
            result.append(item[0])
        elif item[1] < second:
            break
    
    print(*sorted(result))