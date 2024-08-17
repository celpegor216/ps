N, M = map(int, input().split())
lst = []

for n in range(N):
    tmp = list(map(int, input().split()))

    for item in tmp:
        lst.append((item, n))

lst.sort()

bucket = [0] * N
cnt = 0
result = 10 ** 9

start = 0
for end in range(N * M):
    end_num, end_team = lst[end]

    bucket[end_team] += 1
    if bucket[end_team] == 1:
        cnt += 1
    
    while cnt == N:
        start_num, start_team = lst[start]
        result = min(result, end_num - start_num)
        
        bucket[start_team] -= 1
        if not bucket[start_team]:
            cnt -= 1
        start += 1
    
print(result)