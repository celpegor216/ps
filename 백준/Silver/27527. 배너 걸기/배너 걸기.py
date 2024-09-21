from math import ceil

N, M = map(int, input().split())
lst = [0] + list(map(int, input().split()))


def find():
    target_cnt = ceil(9 * M / 10)

    bucket = dict()

    for i in range(M):
        bucket[lst[i]] = bucket.get(lst[i], 0) + 1
        if bucket[lst[i]] == target_cnt:
            return 'YES'

    for i in range(N - M + 1):
        bucket[lst[i]] -= 1
        bucket[lst[i + M]] = bucket.get(lst[i + M], 0) + 1

        if bucket[lst[i + M]] >= target_cnt:
            return 'YES'
    
    return 'NO'


print(find())