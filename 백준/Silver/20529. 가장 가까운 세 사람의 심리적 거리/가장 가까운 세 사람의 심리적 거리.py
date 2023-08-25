T = int(input())

dic = {'E': '0', 'I': '1', 'S': '0', 'N': '1', 'T': '0', 'F': '1', 'J': '0', 'P': '1'}
diffs = [[0] * 16 for _ in range(16)]

for i in range(16):
    for j in range(16):
        a = bin(i)[2:]
        a = '0' * (4 - len(a)) + a
        
        b = bin(j)[2:]
        b = '0' * (4 - len(b)) + b

        for k in range(4):
            if a[k] != b[k]:
                diffs[i][j] += 1

def dfs(level, path):
    global result

    if level == 3:
        total = diffs[path[0]][path[1]] + diffs[path[1]][path[2]] + diffs[path[2]][path[0]]

        result = min(result, total)
        return
    
    for i in range(16):
        if lst[i] > 0:
            lst[i] -= 1
            dfs(level + 1, path + [i])
            lst[i] += 1

for t in range(T):
    N = int(input())
    lst = [0] * 16
    
    temp = input().split()
    for t in temp:
        num = int(dic[t[0]] + dic[t[1]] + dic[t[2]] + dic[t[3]], 2)
        lst[num] += 1
    
    result = 21e8
    dfs(0, [])

    print(result)