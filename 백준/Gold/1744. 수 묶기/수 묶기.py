N = int(input())
lst_p = []
lst_m = []
cnt_zero = 0

for n in range(N):
    num = int(input())

    if num > 0:
        lst_p.append(num)
    elif num < 0:
        lst_m.append(num)
    else:
        cnt_zero += 1

# 음수가 있다면 음수끼리 둘이 묶기(큰거+둘째큰거)
# 양수가 있다면 양수끼리 둘이 묶기(큰거+둘째큰거)
# 음수, 양수 하나씩 남는다면 더하지 않기

total = 0
lst_p.sort(reverse=True)
lst_m.sort()

if len(lst_p) % 2:
    total += lst_p.pop()
if len(lst_m) % 2:
    if not cnt_zero:
        total += lst_m.pop()
    else:
        lst_m.pop()

for i in range(0, len(lst_p), 2):
    temp_plus = lst_p[i] + lst_p[i + 1]
    temp_mult = lst_p[i] * lst_p[i + 1]
    total += max(temp_plus, temp_mult)
for i in range(0, len(lst_m), 2):
    total += lst_m[i] * lst_m[i + 1]

print(total)