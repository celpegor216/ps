N = int(input())
S = input()
bucket = [0] * 3
tmp = 'BSA'
for s in S:
    bucket[tmp.index(s)] += 1

maxv = max(bucket)
res = ''
for i in range(3):
    if bucket[i] == maxv:
        res += tmp[i]

if len(res) == 3:
    print('SCU')
else:
    print(res)