N, M = map(int, input().split())
road = [0] * 100

idx = 0
for _ in range(N):
    length, speed = map(int, input().split())
    for i in range(length):
        road[idx] = speed
        idx += 1

result = 0
now = 0
for _ in range(M):
    length, speed = map(int, input().split())
    for i in range(length):
        result = max(result, speed - road[now])
        now += 1

print(result)