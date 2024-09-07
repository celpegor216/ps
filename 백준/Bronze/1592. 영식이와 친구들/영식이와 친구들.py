N, M, L = map(int, input().split())

cnt = [0] * N

now = 0
result = 0
while 1:
    cnt[now] += 1

    if cnt[now] == M:
        break
    
    if cnt[now] % 2:
        now = (now + L) % N
    else:
        now = (now - L) % N
    
    result += 1

print(result)