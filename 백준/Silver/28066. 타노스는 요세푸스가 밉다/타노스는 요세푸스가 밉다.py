N, K = map(int, input().split())

lst = [n for n in range(1, N + 1)]
length = N

while length > K:
    a = length - (length % K)
    lst = lst[a:] + [lst[n] for n in range(0, a, K)]
    length = len(lst)

print(lst[0])