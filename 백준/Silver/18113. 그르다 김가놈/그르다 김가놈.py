N, K, M = map(int, input().split()) # 김밥 수, 꼬다리 길이, 최소 김밥조각
lst = []

for n in range(N):
    L = int(input())

    if L >= 2 * K:
        lst.append(L - 2 * K)
    elif L > K:
        lst.append(L - K)

result = -1

if lst:
    start, end = 1, max(lst)

    while start <= end:
        middle = (start + end) // 2

        cnt = 0
        for item in lst:
            cnt += item // middle
        
        if cnt >= M:
            result = middle
            start = middle + 1
        else:
            end = middle - 1

print(result)