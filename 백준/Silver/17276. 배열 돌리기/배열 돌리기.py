T = int(input())

def turn_anticlockwise():
    center = N // 2

    for i in range(1, center + 1):
        temp = lst[center - i][center - i]

        lst[center - i][center - i] = lst[center - i][center]
        lst[center - i][center] = lst[center - i][center + i]
        lst[center - i][center + i] = lst[center][center + i]
        lst[center][center + i] = lst[center + i][center + i]
        lst[center + i][center + i] = lst[center + i][center]
        lst[center + i][center] = lst[center + i][center - i]
        lst[center + i][center - i] = lst[center][center - i]
        lst[center][center - i] = temp


def turn_clockwise():
    center = N // 2

    for i in range(1, center + 1):
        temp = lst[center + i][center + i]

        lst[center + i][center + i] = lst[center][center + i]
        lst[center][center + i] = lst[center - i][center + i]
        lst[center - i][center + i] = lst[center - i][center]
        lst[center - i][center] = lst[center - i][center - i]
        lst[center - i][center - i] = lst[center][center - i]
        lst[center][center - i] = lst[center + i][center - i]
        lst[center + i][center - i] = lst[center + i][center]
        lst[center + i][center] = temp


for t in range(T):
    N, D = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    if D < 0:
        for d in range(-D // 45):
            turn_anticlockwise()
    else:
        for d in range(D // 45):
            turn_clockwise()

    for line in lst:
        print(*line)