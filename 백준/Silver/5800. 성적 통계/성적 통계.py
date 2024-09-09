K = int(input())

for k in range(K):
    N, *lst = map(int, input().split())
    lst.sort()

    maxv = lst[-1]
    minv = lst[0]
    largest_gap = 0
    for i in range(N - 1):
        largest_gap = max(largest_gap, lst[i + 1] - lst[i])

    print('Class', k + 1)
    print(f'Max {maxv}, Min {minv}, Largest gap {largest_gap}')