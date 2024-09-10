# 반례 참고


N, S, P = map(int, input().split())
if N:
    lst = list(map(int, input().split())) + [-1] * (P - N)
    result = -1
    rank = [0] * P
    for i in range(P):
        if i == 0 or lst[i - 1] > lst[i]:
            rank[i] = i + 1
        else:
            rank[i] = rank[i - 1]

        if S > lst[i]:
            if S == lst[i - 1]:
                result = rank[i - 1]
            else:
                result = rank[i]
            break

    print(result)
else:
    print(1)