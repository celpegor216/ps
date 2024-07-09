import heapq

A = int(input())
lst_A = list(map(int, input().split()))
B = int(input())
lst_B = list(map(int, input().split()))

q_A = []
for a in range(A):
    heapq.heappush(q_A, (-lst_A[a], a))
q_B = []
for b in range(B):
    heapq.heappush(q_B, (-lst_B[b], b))

result = []
now_a = -1
now_b = -1

while q_A and q_B:
    num, idx_a = heapq.heappop(q_A)

    if idx_a < now_a:
        continue

    while q_B and (-q_B[0][0] > -num or (-q_B[0][0] == -num and q_B[0][1] < now_b)):
        heapq.heappop(q_B)

    if q_B and -q_B[0][0] == -num and now_b < q_B[0][1]:
        result.append(-num)
        now_a = idx_a
        now_b = q_B[0][1]
        heapq.heappop(q_B)

print(len(result))

if result:
    print(*result)