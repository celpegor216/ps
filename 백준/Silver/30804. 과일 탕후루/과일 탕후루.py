N = int(input())
lst = list(map(int, input().split()))

dic = dict()
start = end = 0
result = 0

while end < N:
    dic[lst[end]] = dic.get(lst[end], 0) + 1
    while len(dic) > 2:
        dic[lst[start]] -= 1
        if dic[lst[start]] == 0:
            dic.pop(lst[start])
        start += 1
    
    result = max(result, end - start + 1)
    end += 1

print(result)