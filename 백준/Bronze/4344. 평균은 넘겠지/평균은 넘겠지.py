TC = int(input())

for _ in range(TC):
    N, *lst = map(int, input().split())

    avg = sum(lst) / N
    cnt = 0
    for item in lst:
        if item <= avg:
            cnt += 1

    print(f'{100 * (1 - (cnt / N)):0.3f}%')