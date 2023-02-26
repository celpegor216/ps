def solution(n):
    answer = [[0] * i for i in range(1, n + 1)]

    start = (0, 0)
    now_type = 0
    now_num = 1
    k = n

    while k > 0:
        if now_type == 0:
            for i in range(k):
                answer[start[0] + i][start[1]] = now_num
                now_num += 1
        elif now_type == 1:
            for i in range(k):
                answer[-start[1] - 1][start[1] + i + 1] = now_num
                now_num += 1
        else:
            for i in range(k):
                answer[-start[1] - i - 2][-start[1] - 1] = now_num
                now_num += 1

        k -= 1
        now_type += 1
        if now_type == 3:
            now_type = 0
            start = (start[0] + 2, start[1] + 1)

    result = []
    for line in answer:
        result += line

    return result