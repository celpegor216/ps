def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    else:

        yes_0 = [sticker[0]] * 2

        for i in range(2, len(sticker) - 1):
            yes_0.append(max(yes_0[i - 2] + sticker[i], yes_0[i - 1]))

        no_0 = [0, sticker[1]]

        for i in range(2, len(sticker)):
            no_0.append(max(no_0[i - 2] + sticker[i], no_0[i - 1]))

        return max(yes_0[-1], no_0[-1])