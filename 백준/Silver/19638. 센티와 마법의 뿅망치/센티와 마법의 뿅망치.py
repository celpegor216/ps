import heapq

N, H, T = map(int, input().split())
q = []

for _ in range(N):
    heapq.heappush(q, -int(input()))

# 뿅망치를 아예 쓸 필요가 없는 경우
if -q[0] < H:
    print('YES')
    print(0)
else:
    for t in range(T):
        if -q[0] == 1:
            break

        now = -heapq.heappop(q)
        now //= 2
        heapq.heappush(q, -now)

        if -q[0] < H:
            break

    if -q[0] < H:
        print('YES')
        print(t + 1)
    else:
        print('NO')
        print(-q[0])
