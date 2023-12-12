T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = sorted(map(int, input().split()))

    result = 0

    for item in lst1:
        # item보다 크면서 제일 작은 값 찾기
        start, end = 0, M - 1
        res = M - 1

        while start <= end:
            middle = (start + end) // 2

            if lst2[middle] >= item:
                res = middle
                end = middle - 1
            else:
                start = middle + 1

        if res > 0 and abs(item - lst2[res]) >= abs(item - lst2[res - 1]):
            result += lst2[res - 1]
        else:
            result += lst2[res]
    
    print(result)