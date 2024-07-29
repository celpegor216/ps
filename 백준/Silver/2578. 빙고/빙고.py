N = 5
lst = [list(map(int, input().split())) for _ in range(N)]

calls = []
for _ in range(N):
    calls += list(map(int, input().split()))

horizontal_cnt = [0] * 5
vertical_cnt = [0] * 5
cross_cnt = [0] * 2

def check(call):
    for n in range(N):
        for m in range(N):
            if lst[n][m] == call:
                horizontal_cnt[n] += 1
                vertical_cnt[m] += 1

                if n == m:
                    cross_cnt[0] += 1
                if n + m == N - 1:
                    cross_cnt[1] += 1
                return

for i in range(N ** 2):
    check(calls[i])

    if horizontal_cnt.count(N) + vertical_cnt.count(N) + cross_cnt.count(N) >= 3:
        print(i + 1)
        break