# 해답: https://ddingmin00.tistory.com/entry/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-17071%EB%B2%88-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88-5


from collections import deque


N, K = map(int, input().split())
MAX = 500000

# used[n]: n에 짝수/홀수 시간에 방문했을 때 최소 이동 횟수
used = [[-1] * 2 for _ in range(MAX + 1)]

q = deque()
q.append((N, 0))
used[N][0] = 0

while q:
    now, cnt = q.popleft()

    for nxt in (now + 1, now - 1, now * 2):
        if 0 <= nxt <= MAX and used[nxt][(cnt + 1) % 2] == -1:
            used[nxt][(cnt + 1) % 2] = cnt + 1
            q.append((nxt, cnt + 1))

result = -1
for i in range(MAX + 1):
    K += i
    
    if K > MAX:
        break

    # 예를 들어 K 위치에 수빈이가 4초에 도달했고,
    # 해당 위치에 동생이 4초보다 크거나 같으면서 짝수인 시간에 도착했다면
    # +1, -1 하면서 기다릴 수 있음
    if used[K][i % 2] <= i:
        result = i
        break

print(result)