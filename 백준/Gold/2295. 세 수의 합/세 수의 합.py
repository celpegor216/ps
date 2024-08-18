N = int(input())
lst = [int(input()) for _ in range(N)]

lst.sort()

sub_totals = set()

for i in range(N):
    for j in range(N):
        if lst[i] + lst[j] >= lst[-1]:
            break
        sub_totals.add(lst[i] + lst[j])

sub_totals = sorted(sub_totals)
length = len(sub_totals)

result = 0
for k in range(N - 1, -1, -1):
    for n in range(k):
        start = 0
        end = length - 1
        flag = 0

        while start <= end:
            middle = (start + end) // 2

            if lst[n] + sub_totals[middle] == lst[k]:
                flag = 1
                break
            elif lst[n] + sub_totals[middle] > lst[k]:
                end = middle - 1
            else:
                start = middle + 1
        
        if flag:
            result = lst[k]
            break
    
    if result:
        break

print(result)