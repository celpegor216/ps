N = int(input())

cnt = 1
while N >= cnt:
    N -= cnt
    cnt += 1

print(cnt - N if cnt % 2 else 0)