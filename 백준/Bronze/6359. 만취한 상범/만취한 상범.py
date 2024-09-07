T = int(input())

MAX = 100
lst = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    j = i
    while j <= MAX:
        lst[j] = 1 - lst[j]
        j += i

for _ in range(T):
    N = int(input())
    print(sum(lst[1:N + 1]))