S = input()

if int(S) < 9:
    print(int(S) + 1)
elif int(S) == 9:
    print(11)
else:
    N = len(S)

    result = []
    for n in range(N // 2):
        result.append(int(S[n]))

    if N % 2:
        result += [int(S[N // 2])] + result[::-1]
    else:
        result += result[::-1]

    ranges = [range(N // 2 - 1, 0, -1), range(N // 2, 0, -1)]

    while 1:
        total = 0
        for item in result:
            total = total * 10 + item
        if total > int(S):
            print(total)
            break

        result[N // 2] += 1
        if not N % 2:
            result[N // 2 - 1] += 1

        for i in ranges[N % 2]:
            if result[i] == 10:
                result[i] = 0
                result[i - 1] += 1
                result[-i - 1] = 0
                result[-i] += 1

        if result[0] == 10:
            N += 1
            result = [1] + [0] * (N - 2) + [1]