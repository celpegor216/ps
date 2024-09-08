N = int(input())

MAX = 1000

for _ in range(N):
    V = int(input())
    bucket = [0] * (MAX + 1)

    for _ in range(V):
        bucket[int(input())] += 1
    
    maxv = 0
    maxi = 0
    for i in range(1, MAX + 1):
        if bucket[i] > maxv:
            maxv = bucket[i]
            maxi = i
    
    print(maxi)