N = int(input())
lst = list(set(map(int, input().split())))
N = len(lst)

length = max(lst) + 1
primes = [0] * length

for i in range(2, length):
    j = i * 2
    while j < length:
        primes[j] = 1
        j += i
    
used = [0] * len(lst)

for n in range(N):
    if primes[lst[n]]:
        used[n] = 1

if sum(used) == N:
    print(-1)
else:
    total = 1

    for n in range(N):
        if not used[n]:
            total *= lst[n]
    
    print(total)