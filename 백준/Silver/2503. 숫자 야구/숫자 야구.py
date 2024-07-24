N = int(input())
query = [list(map(int, input().split())) for _ in range(N)]

result = 0
used = [0] * 10

def dfs(level, now):
    global result

    if level == 3:
        flag = 1

        for num, strike, ball in query:
            num = str(num)

            cnt_strike = 0
            cnt_ball = 0

            for i in range(3):
                if now[i] == num[i]:
                    cnt_strike += 1
                elif now[i] in num:
                    cnt_ball += 1

            if cnt_strike != strike or cnt_ball != ball:
                flag = 0
                break

        result += flag
        return

    for i in range(1, 10):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, now + str(i))
            used[i] = 0

dfs(0, '')

print(result)