S = input()
key = input()
key = [ord(i) - ord('a') + 1 for i in key]
length = len(key)
idx = 0

for s in S:
    if s == ' ':
        print(s, end='')
    else:
        tmp = ord(s) - key[idx]
        if tmp < ord('a'):
            tmp += 26
        print(chr(tmp), end='')
    idx = (idx + 1) % length