N, K = map(int, input().split())

result = 'NO'
for n in range(N // 2 + 1):
    tmp = (n + 1) * (N - n + 1)
    if tmp == K:
        result = 'YES'
        break
    elif tmp > K:
        break

print(result)