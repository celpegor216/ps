T = int(input())

for t in range(T):
    D, N = map(int, input().split())
    lst = list(map(int, input().split()))

    dic = dict()

    now = 0

    result = 0

    for n in range(N):
        now += lst[n]
        now %= D

        if not now:
            result += 1

        dic[now] = dic.get(now, 0) + 1

    for key in dic.keys():
        result += dic[key] * (dic[key] - 1) // 2
    
    print(result)