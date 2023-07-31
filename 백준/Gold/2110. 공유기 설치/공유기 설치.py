N, C = map(int, input().split())
lst = [int(input()) for _ in range(N)]

lst.sort()

if C == 2:
    print(lst[-1] - lst[0])
else:
    start = 1
    end = int((lst[-1] - lst[0]) / (C - 2))
    result = 1

    while start <= end:
        middle = (start + end) // 2

        temp = set()

        s, e = 0, 1
        while e < N:
            if lst[e] - lst[s] >= middle:
                temp.add(e)
                temp.add(s)
                s = e
                e = s + 1
            else:
                e += 1

        if len(temp) < C:
            end = middle - 1
        else:
            result = max(result, middle)
            start = middle + 1

    print(result)