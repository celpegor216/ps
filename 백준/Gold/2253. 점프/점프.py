from collections import deque

N, M = map(int, input().split())
lst = [int(input()) for _ in range(M)]

if 2 not in lst:
    dic = dict()
    for i in range(1, N + 1):
        dic[i] = {}
    dic[1] = {1: 0} # 속도, 횟수
    dic[2] = {1: 1}

    q = deque()
    q.append((2, 1, 1))

    while q:
        nows, nowx, nowc = q.popleft()

        for i in range(-1, 2):
            tempx = nowx + i
            temps = nows + tempx
            tempc = nowc + 1
            # 앞으로만 이동하는지, N을 넘지 않는지, 못 갈 수 있는 돌은 아닌지
            if tempx > 0 and temps <= N and temps not in lst:
                # 가려는 곳에 같은 속도로 방문한 적이 있는지, 있다면 횟수가 더 적은지
                if tempx not in dic[temps].keys() or (tempx in dic[temps].keys() and dic[temps][tempx] > tempc):
                    dic[temps][tempx] = tempc
                    q.append((temps, tempx, tempc))

    if dic[N].keys():
        print(min(dic[N].values()))
    else:
        print(-1)
else:
    print(-1)