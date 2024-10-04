TC = 3


def find():
    dp = set()
    dp.add(0)

    for a, b in coins:
        new_dp = set()
        for item in dp:
            for i in range(b + 1):
                if item + a * i > total:
                    continue
                new_dp.add(item + a * i)
        if total in new_dp:
            return 1
        dp = new_dp

    return 0


for _ in range(TC):
    N = int(input())
    coins = []
    total = 0
    cnt = 0

    for _ in range(N):
        a, b = map(int, input().split())
        coins.append((a, b))
        total += a * b
        cnt += b

    if total % 2:
        print(0)
        continue

    total //= 2

    coins.sort()

    print(find())