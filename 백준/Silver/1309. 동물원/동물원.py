# f(1) = 3
# f(2) = 3 * 1 + 2 * 2 = 7
# f(3) = 3 * 3 + 2 * 4 = 17
# f(4) = 3 * 7 + 2 * 10 = 41
# ...
# f(k) = 3 * f(k - 2) + 2 * (f(k - 1) - f(k - 2)) = 2 * f(k - 1) + f(k - 2)

N = int(input())

if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    back_2 = 3
    back_1 = 7
    now = 0

    for n in range(2, N):
        now = 2 * back_1 + back_2
        back_2 = back_1
        back_1 = now

    print(now % 9901)