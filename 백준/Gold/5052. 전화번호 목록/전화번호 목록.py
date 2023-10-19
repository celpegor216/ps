T = int(input())

result = 'YES'

def dfs(level, nowdic, item):
    global result

    if result == 'NO':
        return
    
    if nowdic.get(item[level]):
        if nowdic[item[level]][0] == 1:
            result = 'NO'
            return
        else:
            dfs(level + 1, nowdic[item[level]][1], item)
    else:
        nowdic[item[level]] = [0, dict()]

        if level == len(item) - 1:
            nowdic[item[level]][0] = 1
        else:
            dfs(level + 1, nowdic[item[level]][1], item)


for t in range(T):
    N = int(input())
    lst = [input() for _ in range(N)]
    lst.sort(key=lambda x:(len(x), x))

    result = 'YES'
    dic = dict()

    for item in lst:
        if result != 'NO':
            dfs(0, dic, item)
    
    print(result)