# 시간 줄이려고 아래처럼 풀었는데 오히려 시간이 오래 걸림...

# now = 1
# for n in range(2, N + 1):
#     now *= n

#     while now >= 10 and now % 10 == 0:
#         now //= 10

N = int(input())

now = 1
for n in range(2, N + 1):
    now *= n

now = str(now)
for i in range(len(now) - 1, -1, -1):
    if now[i] != '0':
        print(now[i])
        break