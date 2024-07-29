N, Q = map(int, input().split())
lst = list(map(int, input().split()))
lst_sum = [0] * N

for n in range(N):
    lst_sum[n] = lst[n] * lst[(n + 1) % N] * lst[(n + 2) % N] * lst[(n + 3) % N]

total = sum(lst_sum)

queries = list(map(int, input().split()))

for query in queries:
    query -= 1

    for i in range(4):
        lst_sum[query - i] *= -1
        total += lst_sum[query - i] * 2
    print(total)