D, N = map(int, input().split())
oven = list(map(int, input().split()))    # 위 > 아래, D개
pizza = list(map(int, input().split()))    # 먼저 > 나중, N개

# oven_min[i]: oven의 i번째 위치까지 올 수 있는 최대값
oven_min = [21e8] * D
for d in range(D):
    oven_min[d] = min(oven_min[d - 1], oven[d])

# 이전 피자가 사용한 오븐
last_used = D
for n in range(N):
    if last_used == 0:
        last_used = -1
        break

    start = 0
    end = last_used - 1
    use = -1
    while start <= end:
        middle = (start + end) // 2

        if oven_min[middle] >= pizza[n]:
            use = max(use, middle)
            start = middle + 1
        else:
            end = middle - 1

    if use == -1:
        last_used = -1
        break

    last_used = use

print(last_used + 1)