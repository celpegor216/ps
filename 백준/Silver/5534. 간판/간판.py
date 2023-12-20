N = int(input())
new = input()
olds = [input() for _ in range(N)]

length = len(new)
result = 0

for old in olds:
    for i in range(len(old)):
        if old[i] == new[0]:
            check = 0

            for j in range(i + 1, len(old)):
                if old[j] == new[1]:
                    diff = j - i
                    
                    flag = 0

                    for n in range(1, length):
                        if i + diff * n < len(old) and old[i + diff * n] == new[n]:
                            continue
                        else:
                            flag = 1
                            break
                    
                    if not flag:
                        result += 1
                        check = 1
                        break
            
            if check:
                break

print(result)