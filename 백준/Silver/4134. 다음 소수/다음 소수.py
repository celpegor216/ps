T = int(input())

for _ in range(T):
    N = int(input())
    
    if N < 2:
        print(2)
        continue

    while 1:
        half = int(N ** 0.5) + 1

        flag = 0
        for i in range(2, half):
            if not N % i:
                flag = 1
                break
        
        if flag:
            N += 1
        else:
            print(N)
            break