lst = [
    ['000000', 'A'],
    ['001111', 'B'],
    ['010011', 'C'],
    ['011100', 'D'],
    ['100110', 'E'],
    ['101001', 'F'],
    ['110101', 'G'],
    ['111010', 'H'],
]

N = int(input())
S = input()

result = ''
for n in range(N):
    now = S[6 * n:6 * (n + 1)]
    
    checks = [0] * 8
    for i in range(8):
        for j in range(6):
            if now[j] != lst[i][0][j]:
                checks[i] += 1
    
    minv = 6
    result_idx = -1
    for i in range(8):
        if checks[i] < minv:
            minv = checks[i]
            result_idx = i
    
    if minv > 1:
        print(n + 1)
        break
    
    result += lst[result_idx][1]
else:
    print(result)