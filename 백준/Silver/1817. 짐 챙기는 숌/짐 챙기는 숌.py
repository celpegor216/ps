N, M = map(int, input().split())

if not N:

    print(0)

else:

    lst = list(map(int, input().split()))

    result = 1

    now = 0

    for item in lst:

        if now + item <= M:

            now += item

        else:

            result += 1

            now = item

    

    print(result)