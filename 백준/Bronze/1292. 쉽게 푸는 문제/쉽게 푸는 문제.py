A, B = map(int, input().split())

lst = [0] * B

cnt = 1
idx = 0
while idx < B:
    for i in range(cnt):
        lst[idx] = cnt
        idx += 1

        if idx == B:
            break
    cnt += 1

print(sum(lst) - sum(lst[:A - 1]))