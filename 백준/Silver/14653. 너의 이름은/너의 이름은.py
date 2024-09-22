# 아예 모르겠음,,,
# 해답: https://nbalance97.tistory.com/224


N, K, Q = map(int, input().split())
lst = [input().split() for _ in range(K)]
Q -= 1

not_read = set([chr(ord('A') + n) for n in range(1, N)])

# Q 이전에 메시지를 보낸 사람들 전부 제거
for k in range(Q, K):
    not_read.discard(lst[k][1])

# Q와 메시지를 읽지 않은 사람 수가 같을 때
# 메시지를 보낸 사람들 전부 제거
for k in range(Q - 1, -1, -1):
    if lst[k][0] != lst[Q][0]:
        break
    not_read.discard(lst[k][1])

not_read = sorted(not_read)

if not not_read or lst[Q][0] == '0':
    print(-1)
else:
    print(*not_read)