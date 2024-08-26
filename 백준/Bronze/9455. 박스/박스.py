T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    # lst[m]: m번째 열에 있는 모든 박스의 행 좌표
    lst = [[] for _ in range(M)]

    for n in range(N):
        tmp = list(map(int, input().split()))
        for m in range(M):
            if tmp[m]:
                lst[m].append(n)

    result = 0
    for m in range(M):
        length = len(lst[m])
        for i in range(length):
            # N - length + i: lst[m][i]가 도착해야 하는 위치
            result += (N - length + i) - lst[m][i]

    print(result)