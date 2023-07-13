N, W = map(int, input().split())
lst = [int(input()) for _ in range(N)]

coin = 0

for i in range(N - 1):
    if lst[i] < lst[i + 1] and W >= lst[i]:
        coin += W // lst[i]
        W = W % lst[i]
    elif lst[i] > lst[i + 1] and coin:
        W += coin * lst[i]
        coin = 0

print(W + coin * lst[-1])