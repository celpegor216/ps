T = int(input())

for t in range(T):
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    lst.sort()

    for n in range(N):
        temp = [1]

        half = int(lst[n] ** 0.5)
        for i in range(2, half + 1):
            if not lst[n] % i:
                temp.append(i)
                temp.append(lst[n] // i)
        
        temp.append(lst[n])
        lst[n] = sorted(temp)

    total = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(len(lst[i]) - 1, -1, -1):
                if lst[i][k] in lst[j]:
                    total += lst[i][k]
                    break
    
    print(total)