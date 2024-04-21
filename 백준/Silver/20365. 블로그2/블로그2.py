N = int(input())
S = input()

cnt_R = 0
cnt_B = 0
now = ''

for n in range(N):
    if S[n] != now:
        now = S[n]
        if now == 'R':
            cnt_R += 1
        else:
            cnt_B += 1

print(min(cnt_R, cnt_B) + 1)