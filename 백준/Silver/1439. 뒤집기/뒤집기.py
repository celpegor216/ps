S = input()

cnt_0 = 0
cnt_1 = 0

now = ''

for item in S:
    if item != now:
        if item == '0':
            cnt_0 += 1
        else:
            cnt_1 += 1
        now = item

print(min(cnt_0, cnt_1))