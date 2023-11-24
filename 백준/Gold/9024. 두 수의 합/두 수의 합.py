T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    lst = sorted(map(int, input().split()))

    minv = 21e9
    cnt = 0

    left, right = 0, N - 1

    while left < right:
        tmp = lst[left] + lst[right]

        diff = abs(K - tmp)

        if diff < minv:
            minv = diff
            cnt = 1
        elif diff == minv:
            cnt += 1
        
        if tmp < K:
            left += 1
        else:
            right -= 1
    
    print(cnt)