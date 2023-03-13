from itertools import combinations

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

result = 21e8

def calc(lst):
    res = 0
    
    for i in range(n // 2):
        for j in range(n // 2):
            res += li[lst[i]][lst[j]]
    
    return res

for combi in combinations([x for x in range(n)], n // 2):
    total_s = calc(combi)
    total_l = calc([x for x in range(n) if x not in combi])
    
    result = min(result, abs(total_l - total_s))

print(result)