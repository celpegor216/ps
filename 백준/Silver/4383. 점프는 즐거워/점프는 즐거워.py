while 1:
    try:
        lst = list(map(int, input().split()))
        N = lst[0]

        result = 'Jolly'
        used = [0] * N
        for i in range(1, N):
            diff = abs(lst[i] - lst[i + 1])
            if not diff or diff >= N or used[diff]:
                result = 'Not jolly'
                break
            used[diff] = 1

        if sum(used[1:]) != N - 1:
            result = 'Not jolly'

        print(result)
    except:
        break