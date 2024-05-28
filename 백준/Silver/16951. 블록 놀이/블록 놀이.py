# 해답: https://100100e.tistory.com/375

N, K = map(int, input().split())
lst = list(map(int, input().split()))

result = N - 1

# 기준값
for i in range(N):
    cnt = 0
    tmp = [0] * N

    for j in range(N):
        if i > j:
            tmp[j] = lst[i] - K * (i - j)
        else:
            tmp[j] = lst[i] + K * (j - i)
        
        if tmp[j] <= 0:
            cnt = N - 1
            break
        elif tmp[j] != lst[j]:
            cnt += 1

    result = min(cnt, result)

print(result)