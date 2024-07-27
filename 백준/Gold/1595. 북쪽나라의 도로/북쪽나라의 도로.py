import sys
input = sys.stdin.readline

N = 10000
cities = dict()

try:
    while 1:
        a, b, c = map(int, input().split())
        cities[a] = cities.get(a, []) + [(c, b)]
        cities[b] = cities.get(b, []) + [(c, a)]
except:
    pass

def find(now):
    if len(cities[now]) == 1:
        return [0]
    else:
        tmp = []

        for cost, next in cities[now]:
            if not used[next]:
                used[next] = 1
                tmp.append(cost + max(find(next)))
        
        return tmp

if not cities:
    print(0)
elif len(cities) < 3:
    for value in cities.values():
        print(value[0][0])
        break
else:
    used = [0] * (N + 1)
    for key, value in cities.items():
        if len(value) > 1:
            used[key] = 1
            print(sum(sorted(find(key))[-2:]))
            break