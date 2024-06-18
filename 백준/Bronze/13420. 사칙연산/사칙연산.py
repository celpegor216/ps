T = int(input())

for _ in range(T):
    lst = input().split()
    lst[0] = int(lst[0])
    lst[2] = int(lst[2])
    lst[4] = int(lst[4])

    result = 0

    if lst[1] == '+':
        result = lst[0] + lst[2]
    elif lst[1] == '-':
        result = lst[0] - lst[2]
    elif lst[1] == '*':
        result = lst[0] * lst[2]
    elif lst[1] == '/':
        result = lst[0] / lst[2]

    if result == lst[4]:
        print("correct")
    else:
        print("wrong answer")