S = input()
N = len(S)

def find():
    now = 1
    length = 1
    idx = 0
    while 1:
        tmp = str(now)
        for i in range(length):
            if S[idx] == tmp[i]:
                idx += 1

            if idx == N:
                return now

        now += 1
        if now == 10 ** length:
            length += 1

print(find())