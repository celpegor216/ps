N = int(input())
lst = [n for n in range(1, N + 1)]
head = 0
t = 1

while N > 1:
    target = (head + (t ** 3 - 1)) % N
    lst.pop(target)
    N -= 1
    t += 1
    head = target % N

print(lst[0])