from collections import deque

N = int(input())
result = [0] * N

# q: 배치할 수 있는 남은 위치
q = deque(range(N))

for n in range(1, N + 1):
    # 남은 카드 중 첫 번째 카드를 뒤로 옮기는 걸 반복해야 하는 횟수
    # N - n + 1: q의 길이
    # q의 길이보다 이동해야 하는 횟수가 클 경우,
    # q의 길이만큼 이동하면 어차피 한 바퀴 돌아서 원상태가 되므로
    # q의 길이로 나눴을 때 나눈 나머지만큼만 이동하면 됨
    move = n % (N - n + 1)

    for _ in range(move):
        q.append(q.popleft())

    # q의 맨 앞에 있는 위치에 n을 배치
    result[q.popleft()] = n

print(*result)