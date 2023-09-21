# 해답: https://kau-algorithm.tistory.com/970

N = int(input())
lst = sorted(list(map(int, input().split())))

if N <= 2:
    print(N)
else:
    result = 2

    for start in range(N - 2):
        end = start + 2

        while end < N:
            if lst[start] + lst[start + 1] <= lst[end]:
                break
            result = max(result, end - start + 1)
            end += 1

    print(result)