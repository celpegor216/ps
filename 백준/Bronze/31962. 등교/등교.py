# 학교에 지각하지 않는 시각에 도착하는 버스 중에서,
# 가장 늦게 출발하는 버스가 출발할 때까지 걸리는 시간

N, X = map(int, input().split())

result = -1
for _ in range(N):
    S, T = map(int, input().split())
    if S + T <= X:
        result = max(result, S)

print(result)