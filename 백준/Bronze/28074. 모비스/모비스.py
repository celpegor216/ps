S = input()

flag = 0
target = 'MOBIS'

for t in target:
    if t not in S:
        flag = 1
        break

print('NO' if flag else 'YES')