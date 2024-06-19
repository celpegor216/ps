lst = []
L = 0

while 1:
    try:
        lst.append(input().strip().split())
        L = max(L, len(lst[-1]))
    except:
        break

lengths = [0] * L

for l in range(L):
    for sentence in lst:
        if len(sentence) > l:
            lengths[l] = max(lengths[l], len(sentence[l]))

for sentence in lst:
    tmp = ''
    for i in range(len(sentence)):
        tmp += sentence[i] + ' ' * (lengths[i] - len(sentence[i]) + 1)
    print(tmp.strip())