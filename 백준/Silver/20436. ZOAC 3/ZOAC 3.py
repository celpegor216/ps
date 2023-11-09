l, r = input().split()

lst = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
dic = dict()

for i in range(3):
    for j in range(len(lst[i])):
        dic[lst[i][j]] = (i, j)

result = 0

left = 'qwertasdfgzxcv'

S = input()

for s in S:
    if s in left:
        result += abs(dic[l][0] - dic[s][0]) + abs(dic[l][1] - dic[s][1])
        l = s
    else:
        result += abs(dic[r][0] - dic[s][0]) + abs(dic[r][1] - dic[s][1])
        r = s
    
    result += 1

print(result)