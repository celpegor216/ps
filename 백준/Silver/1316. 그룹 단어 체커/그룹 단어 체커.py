N = int(input())

result = 0
for n in range(N):
    S = input()

    now = S[0]
    used = [now]

    flag = 0
    for i in range(1, len(S)):
        if S[i] != now:
            if S[i] in used:
                flag = 1
                break
            else:
                now = S[i]
                used.append(now)
    
    if not flag:
        result += 1

print(result)