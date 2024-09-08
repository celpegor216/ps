N = int(input())
lst = [input() for _ in range(N)]

def check():
    for i in range(N):
        for j in range(i + 1):
            if lst[i][j] != lst[j][i]:
                return 'NO'
    
    return 'YES'

print(check())