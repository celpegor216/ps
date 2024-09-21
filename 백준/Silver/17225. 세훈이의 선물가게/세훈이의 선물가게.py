import heapq


A, B, N = map(int, input().split())
q = []

# 주문 시각, 포장지 색, 선물 개수
# 시각 오름차순, 같은 시각 주문 X
ends = [0] * 2
for _ in range(N):
    t, c, m = input().split()
    t, m = int(t), int(m)
    c = 0 if c == 'B' else 1

    time = t if ends[c] < t else ends[c]

    for i in range(m):
        heapq.heappush(q, (time, c))
        time += B if c else A
    
    ends[c] = time

results = [[] for _ in range(2)]
present_idx = 1

while q:
    _, color = heapq.heappop(q)

    results[color].append(present_idx)
    present_idx += 1

for result in results:
    print(len(result))
    print(*result)