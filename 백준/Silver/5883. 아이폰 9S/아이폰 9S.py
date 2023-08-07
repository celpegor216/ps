N = int(input())
lst = [int(input()) for _ in range(N)]
sett = set(lst)

result = 1
for item in sett:
    temp = [x for x in lst if x != item]

    cnt = 1
    now = temp[0]

    for i in range(1, len(temp)):
        if temp[i] == now:
            cnt += 1
        else:
            result = max(result, cnt)
            cnt = 1
            now = temp[i]
    
    result = max(result, cnt)
    
print(result)