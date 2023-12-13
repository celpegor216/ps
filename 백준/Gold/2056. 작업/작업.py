N = int(input())
time = [0] * (N + 1)

for n in range(N):
    lst = list(map(int, input().split()))

    time[n + 1] = lst[0]

    maxv = 0
    for i in range(lst[1]):
        if time[lst[i + 2]] > maxv:
            maxv = time[lst[i + 2]]
    
    time[n + 1] += maxv

print(max(time))