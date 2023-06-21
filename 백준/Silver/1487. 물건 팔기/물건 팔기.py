N = int(input())
lst = []

for n in range(N):
    a, b = map(int, input().split())

    if a > b:
        lst.append([a, b])

N = len(lst)
maxt = 0
maxv = 0

for n in range(N):
    total = 0

    for i in range(N):
        if lst[i][0] >= lst[n][0] and lst[n][0] >= lst[i][1]:
            total += lst[n][0] - lst[i][1]
    
    if total > maxt or (total == maxt and lst[n][0] < maxv):
        maxt = total
        maxv = lst[n][0]

print(maxv)