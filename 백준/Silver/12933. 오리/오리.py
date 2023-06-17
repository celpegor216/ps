s = list(input())
quack = 'quack'
used = [0]

for item in s:
    flag = 0

    for i in range(len(used)):
        if quack[used[i]] == item:
            used[i] += 1
            if used[i] == 5:
                used[i] = 0
            flag = 1
            break
    
    if not flag:
        used.append(1)

if sum(used):
    print(-1)
else:
    print(len(used))