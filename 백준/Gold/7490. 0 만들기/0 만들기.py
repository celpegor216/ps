T = int(input())

calcs = [' ', '+', '-']

def dfs(level, path):
    
    if level == N:
        a = 0
        calc = '+'
        b = 1

        for i in range(1, level):
            if path[i * 2 - 1] == ' ':
                b = b * 10 + int(path[i * 2])
            else:
                if calc == '+':
                    a += b
                else:
                    a -= b
                calc = path[i * 2 - 1]
                b = int(path[i * 2])
        
        if calc == '+':
            a += b
        else:
            a -= b

        if a == 0:
            print(path)

        return
    
    for c in calcs:
        dfs(level + 1, path + c + str(level + 1))

for t in range(T):
    N = int(input())

    dfs(1, '1')

    print()