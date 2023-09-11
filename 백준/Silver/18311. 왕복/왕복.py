N, K = map(int, input().split())
lst = list(map(int, input().split()))

now = 0
result = -1

for n in range(N):
    if now <= K < now + lst[n]:
        result = n
        break
    now += lst[n]

if result == -1:
    for n in range(N - 1, -1, -1):
        if now <= K < now + lst[n]:
            result = n
            break
        now += lst[n]

print(result + 1)