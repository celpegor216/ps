N = int(input())
lst = list(map(int, input().split()))
calcs = list(map(int, input().split())) # + - * //
table = '+-*/'

minv, maxv = 10e11, -10e11

def dfs(level, path):
    global minv, maxv

    if level == N - 1:
        total = lst[0]

        for i in range(N - 1):
            if path[i] == '+':
                total += lst[i + 1]
            elif path[i] == '-':
                total -= lst[i + 1]
            elif path[i] == '*':
                total *= lst[i + 1]
            else:
                if total > 0:
                    total //= lst[i + 1]
                elif total < 0:
                    total = -(-total // lst[i + 1])
        
        if total > maxv:
            maxv = total
        
        if total < minv:
            minv = total
        
        return
    
    for i in range(4):
        if calcs[i] > 0:
            calcs[i] -= 1
            dfs(level + 1, path + table[i])
            calcs[i] += 1

dfs(0, '')

print(maxv)
print(minv)