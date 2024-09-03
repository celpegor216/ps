N, X = map(int, input().split())
lst = list(map(int, input().split()))

idx = 0
while 1:
    if lst[idx] < X:
        print(idx + 1)
        break
    idx = (idx + 1) % N
    X += 1