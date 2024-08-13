N = int(input())
lst = list(map(int, input().split()))

result = now = lst[0]

for n in range(1, N):
    # 지금까지 더한 합(now)에 지금 것을 더한 것보다 지금 것의 값이 더 큰 경우
    # 아예 now를 쓰지 않는 것이 좋음
    if now + lst[n] < lst[n]:
        now = lst[n]
    else:
        now += lst[n]
    result = max(result, now)

print(result)