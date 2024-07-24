N = int(input())

now = 666
result = 0

while result < N:
    if '666' in str(now):
        result += 1
    now += 1

print(now - 1)