N, M = map(int, input().split())
lst_set = []
lst_one = []

for _ in range(M):
    a, b = map(int, input().split())
    lst_set.append(a)
    lst_one.append(b)

lst_set.sort()
lst_one.sort()

betters = [0] * 7

for i in range(1, 7):
    if lst_set[0] < lst_one[0] * i:
        betters[i] = lst_set[0]
    else:
        betters[i] = lst_one[0] * i

print((N // 6) * betters[-1] + betters[N % 6])