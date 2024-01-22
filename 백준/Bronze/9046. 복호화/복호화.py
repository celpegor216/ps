T = int(input())

for t in range(T):
    S = input()
    bucket = [0] * 26

    for s in S:
        if s != ' ':
            bucket[ord(s) - ord('a')] += 1

    maxv = 0
    maxidx = 0

    for i in range(26):
        if bucket[i] > maxv:
            maxv = bucket[i]
            maxidx = i
        elif bucket[i] == maxv:
            maxidx = -1
    
    if maxidx == -1:
        print('?')
    else:
        print(chr(ord('a') + maxidx))