N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 최솟값이 max(lst)보다 작으면 max(lst)를 담을 수 있는 블루레이가 없을 수 있음
start = max(lst)
end = sum(lst)
result = end

while start <= end:
    middle = (start + end) // 2

    cnt = 1
    now = 0
    for n in range(N):
        if now + lst[n] > middle:
            cnt += 1
            now = lst[n]
        else:
            now += lst[n]

    if cnt <= M:    # M개 이하로 사용해도 된다...
        result = min(result, middle)
        end = middle - 1
    else:
        start = middle + 1

print(result)