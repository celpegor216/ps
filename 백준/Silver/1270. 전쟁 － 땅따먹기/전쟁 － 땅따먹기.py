T = int(input())

for _ in range(T):
    N, *lst = map(int, input().split())

    bucket = dict()
    for item in lst:
        bucket[item] = bucket.get(item, 0) + 1

    result = sorted(bucket.items(), key=lambda x: -x[1])
    if result[0][1] > N // 2:
        print(result[0][0])
    else:
        print('SYJKGW')