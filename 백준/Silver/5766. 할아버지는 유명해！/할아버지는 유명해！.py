while 1:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    bucket = dict()

    for _ in range(N):
        tmp = map(int, input().split())
        for key in tmp:
            bucket[key] = bucket.get(key, 0) + 1

    bucket = sorted(bucket.items(), key=lambda x: (-x[1], x[0]))
    maxv = bucket[1][1]
    result = []

    for idx, v in bucket[1:]:
        if maxv == v:
            result.append(idx)
        else:
            break

    print(*result)