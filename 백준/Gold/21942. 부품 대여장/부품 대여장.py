import sys
input = sys.stdin.readline

import datetime

N, L, F = input().split()

N = int(N)
day, time = L.split('/')
L = int(day) * 24 * 60 + int(time.split(':')[0]) * 60 + int(time.split(':')[1])
F = int(F)

dic = dict()

results = dict()

for n in range(N):
    day, time, unit, name = input().split()
    dt = datetime.datetime.strptime(f'{day} {time}', '%Y-%m-%d %H:%M')

    key = f'{unit} {name}'

    if dic.get(key):
        time_delta = dt - dic[key][0]
        time_delta = time_delta.days * 24 * 60 + time_delta.seconds // 60

        if time_delta > L:
            if results.get(name):
                results[name] += (time_delta - L) * F
            else:
                results[name] = (time_delta - L) * F
        
        dic.pop(key)
    else:
        dic[key] = [dt, name]

if not results:
    print(-1)
else:
    for key in sorted(results.keys()):
        print(key, results[key])