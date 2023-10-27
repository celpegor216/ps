N = int(input())
lst = [int(input()) for _ in range(N)]

left, right = 1, 1

now = lst[0]
for n in range(1, N):
    if lst[n] > now:
        left += 1
        now = lst[n]

now = lst[-1]
for n in range(N - 2, -1, -1):
    if lst[n] > now:
        right += 1
        now = lst[n]

print(left)
print(right)