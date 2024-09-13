from collections import deque

# N 개의 컨테이너들을 적재, 우선순위는 1 이상 M 이하의 정수
# 우선순위가 1에 가까울 수록 높은 우선순위를 가지고, M에 가까울 수록 낮은 우선순위
# M개의 각 우선순위에 대하여 해당 우선순위를 갖는 컨테이너가 적어도 하나 존재
N, M = map(int, input().split())
q = deque()
# 우선순위 별 컨테이너 수
cnts = [0] * (M + 1)

# 우선순위 P, 무게 W
# 레일에 배치되는 순서는 입력으로 주어지는 컨테이너의 순서와 동일
for _ in range(N):
    P, W = map(int, input().split())
    cnts[P] += 1
    q.append((P, W))

result = 0
stored = []
for m in range(M, 0, -1):
    while cnts[m]:
        # 우선순위가 낮은 컨테이너를 먼저 적재
        # 낮은 우선순위의 컨테이너들이 모두 적재되지 않은 상태에서 높은 우선순위의 컨테이너가 온다면 레일의 처음으로 보낸다
        # 레일의 처음으로 보낼 때, 컨테이너의 무게만큼 비용이 발생
        if q[0][0] != m:
            result += q[0][1]
            q.append(q.popleft())
            continue

        # 낮은 우선순위의 컨테이너가 온다면, 무조건 적재
        # 컨테이너의 우선순위가 같을 땐, 무게가 무거운 컨테이너를 아래에 위치시킨다.
        # 우선순위는 같으나, 무게가 가벼운 컨테이너가 먼저 적재돼 있을 경우,
        # 가벼운 컨테이너가 무거운 컨테이너 위로 갈 수 있도록 컨테이너를 빼내고 다시 적재
        # 이 과정을, 가벼운 컨테이너가 모두 빠질 때까지 반복한다.
        # 이 과정에서 컨테이너를 뺄 때와 적재될 때 컨테이너의 무게만큼 비용이 발생
        moved = []
        moved_total = 0
        while stored and stored[-1][0] == q[0][0] and stored[-1][1] < q[0][1]:
            moved_total += stored[-1][1]
            moved.append(stored.pop())

        result += moved_total * 2 + q[0][1]
        stored.append(q.popleft())
        stored += moved[::-1]

        cnts[m] -= 1

print(result)