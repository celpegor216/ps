# 반례 참고

N = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_starts = [0] * 12
for i in range(1, 12):
    month_starts[i] += month_starts[i - 1] + days[i - 1]

lst = []

for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    if em < 3 or sm > 11:
        continue
    s = month_starts[sm - 1] + sd - 1
    e = month_starts[em - 1] + ed - 1
    lst.append((s, e))

lst.sort(key=lambda x: (x[0], -x[1]))
N = len(lst)

stack = []

result = N + 1
for n in range(N):
    if not stack:
        if lst[n][0] <= month_starts[2]:
            stack.append(lst[n])
    else:
        # 연결이 안 되는 경우
        if stack[-1][1] < lst[n][0]:
            break
        # 이미 들어있는 영역에 포함된 경우
        elif stack[0][0] <= lst[n][0] and lst[n][1] <= stack[-1][1]:
            continue
        else:
            while len(stack) > 1 and lst[n][0] <= stack[-2][1] and stack[-1][1] <= lst[n][1]:
                stack.pop()
            
            if len(stack) == 1:
                if lst[n][0] <= month_starts[2] and stack[-1][1] <= lst[n][1]:
                    stack.pop()
            stack.append(lst[n])

    if stack and stack[-1][1] >= month_starts[-1]:
        result = min(result, len(stack))

print(result if result <= N else 0)