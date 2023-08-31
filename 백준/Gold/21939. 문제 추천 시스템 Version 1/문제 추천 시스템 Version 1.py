N = int(input())
problems = dict()
levels = [[] for _ in range(101)]

for n in range(N):
    P, L = map(int, input().split())

    if P in problems.keys():
        problems[P].append(L)
    else:
        problems[P] = [L]
    
    levels[L].append(P)

M = int(input())

for m in range(M):
    tmp = input().split()

    if tmp[0] == 'recommend':
        if tmp[1] == '1':
            for n in range(100, -1, -1):
                if levels[n]:
                    print(max(levels[n]))
                    break
        elif tmp[1] == '-1':
            for n in range(1, 101):
                if levels[n]:
                    print(min(levels[n]))
                    break
    elif tmp[0] == 'add':
        P, L = int(tmp[1]), int(tmp[2])

        if P in problems.keys():
            problems[P].append(L)
        else:
            problems[P] = [L]
        
        levels[L].append(P)
    elif tmp[0] == 'solved':
        P = int(tmp[1])

        lst = problems.pop(P)
        for item in lst:
            levels[item].remove(P)