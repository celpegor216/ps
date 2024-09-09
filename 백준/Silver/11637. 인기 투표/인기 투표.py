T = int(input())

for _ in range(T):
    N = int(input())
    lst = [int(input()) for _ in range(N)]

    maxv = max(lst)

    if lst.count(maxv) > 1:
        print('no winner')
    else:
        idx = lst.index(maxv)
        if maxv > sum(lst) / 2:
            print(f'majority winner {idx + 1}')
        else:
            print(f'minority winner {idx + 1}')