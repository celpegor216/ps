N = int(input())

dic = dict()

for n in range(N):
    lst = input().split()

    now = dic

    for m in range(1, int(lst[0]) + 1):
        if not now.get(lst[m]):
            now[lst[m]] = dict()
        now = now[lst[m]]

def fun(level, now):
    if not now:
        return
    
    for key in sorted(now.keys()):
        print('-' * level * 2 + key)
        fun(level + 1, now[key])

fun(0, dic)