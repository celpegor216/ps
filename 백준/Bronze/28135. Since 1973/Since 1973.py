N = int(input())

cnt = 0
target = '50'
for i in range(N):
    cnt += 1
    if target in str(i):
        cnt += 1
print(cnt)