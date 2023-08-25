# 각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다.

from collections import deque

N = int(input())
nums = [0] + list(map(int, input().split()))
lst = [[]]

for n in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp[1:])

result = 21e8

# 두 팀으로 나눔
for i in range(1, 2 ** N - 1):
    tmp = bin(i)[2:]
    tmp = '0' * (N - len(tmp)) + tmp

    team0 = [x + 1 for x in range(N) if tmp[x] == '0']
    team1 = [x + 1 for x in range(N) if tmp[x] == '1']

    # 나눠진 팀들이 연결되어 있는지 확인
    q = deque()
    q.append(team0[0])
    used = [0] * (N + 1)
    used[team0[0]] = 1

    while q:
        now = q.popleft()

        for item in lst[now]:
            if item in team0 and not used[item]:
                used[item] = 1
                q.append(item)

    flag = 0
    for i in range(1, N + 1):
        if i in team0 and not used[i]:
            flag = 1
            break

    if flag:
        continue
    
    q = deque()
    q.append(team1[0])
    used = [0] * (N + 1)
    used[team1[0]] = 1

    while q:
        now = q.popleft()

        for item in lst[now]:
            if item in team1 and not used[item]:
                used[item] = 1
                q.append(item)
    
    flag = 0
    for i in range(1, N + 1):
        if i in team1 and not used[i]:
            flag = 1
            break

    if flag:
        continue

    # 연결되어 있다면 인구 차이 최솟값 구하기
    result = min(result, abs(sum([nums[x] for x in team0]) - sum([nums[x] for x in team1])))

if result == 21e8:
    print(-1)
else:
    print(result)