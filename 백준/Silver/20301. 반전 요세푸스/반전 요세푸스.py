N, K, M = map(int, input().split())
lst = [n for n in range(1, N + 1)]
head = K - 1
m = 0
while 1:
    print(lst.pop(head))
    m += 1
    if m == M:
        K *= -1
        m = 0
    N -= 1
    if not N:
        break
    head %= N
    if K > 0:
        head = (head + K - 1) % N
    else:
        head = (head + K) % N