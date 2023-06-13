T = int(input())

for t in range(T):
    N = int(input())

    maxname, maxv = '', 0

    for n in range(N):
        name, v = input().split()
        v = int(v)

        if v > maxv:
            maxname = name
            maxv = v
    
    print(maxname)