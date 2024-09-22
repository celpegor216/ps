N = int(input())
lst = [int(input()) - 1 for _ in range(N)]


def find():
    MAX = max(lst) + 1
    q = [0] * MAX

    n = 0
    finished = 0
    result = 0
    while 1:
        for i in range(MAX - 1, -1, -1):
            if not q[i]:
                continue

            # 짐을 넣고 있는 중
            if q[i][0] == i:
                if not q[i][1]:
                    q[i] = 0
                    finished += 1
                    if finished == N:
                        return result
                    continue

                q[i][1] -= 1
            # 이동
            elif not q[i + 1]:
                q[i + 1] = q[i][:]
                q[i] = 0
        
        # 새로운 승객이 들어갈 수 있는 경우
        if n < N and not q[0]:
            q[0] = [lst[n], 4]
            n += 1
        
        result += 1


print(find())