A = int(input())
T = int(input())
N = int(input())

cnt_0 = 0
cnt_1 = 0
now = -1
result = -1

for n in range(1, T + 1):
    for i in range(2):
        cnt_0 += 1
        now = (now + 1) % A

        if N == 0 and cnt_0 == T:
            result = now
            break

        cnt_1 += 1
        now = (now + 1) % A

        if N == 1 and cnt_1 == T:
            result = now
            break

    for j in range(n + 1):
        cnt_0 += 1
        now = (now + 1) % A

        if N == 0 and cnt_0 == T:
            result = now
            break
    
    for j in range(n + 1):
        cnt_1 += 1
        now = (now + 1) % A

        if N == 1 and cnt_1 == T:
            result = now
            break
    
    if result != -1:
        break

print(result)