N, D, K, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]

dic = dict()

for i in range(K):
    if dic.get(lst[i]):
        dic[lst[i]] += 1
    else:
        dic[lst[i]] = 1

result = 0
for n in range(N):
    if dic.get(C):
        result = max(result, len(dic))
    else:
        result = max(result, len(dic) + 1)
    
    if dic[lst[n]] == 1:
        dic.pop(lst[n])
    else:
        dic[lst[n]] -= 1
    
    next_idx = (n + K) % N
    if dic.get(lst[next_idx]):
        dic[lst[next_idx]] += 1
    else:
        dic[lst[next_idx]] = 1

print(result)