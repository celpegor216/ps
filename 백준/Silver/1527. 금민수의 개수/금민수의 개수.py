A, B = map(int, input().split())

result = 0

length = len(str(A))
now = [0] * length

def calc():
    value = 0

    for i in range(length):
        if now[i] == 0:
            value = value * 10 + 4
        else:
            value = value * 10 + 7
    
    return value

while 1:
    value = calc()

    if value > B:
        break

    if A <= value <= B:
        result += 1

    now[-1] += 1

    for i in range(length - 1, 0, -1):
        if now[i] == 2:
            now[i] = 0
            now[i - 1] += 1
    
    if now[0] == 2:
        now = [0, 0] + now[1:]
        length += 1

print(result)