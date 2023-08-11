import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
places = sorted(map(int, input().split()))
animals = []

for n in range(N):
    a, b = map(int, input().split())

    if b <= L:
        animals.append((a, b))

animals.sort(key=lambda x: x[0])
N = len(animals)

p = 0
a = 0

total = 0
while a < N:
    temp = abs(places[p] - animals[a][0]) + animals[a][1]
    
    if temp <= L:
        total += 1
        a += 1
    else:
        if p < M - 1:
            p += 1
        elif p == M - 1:
            a += 1

print(total)