N = int(input())

pills = dict()
for _ in range(N):
    key, value = map(int, input().split())
    pills[key] = value

R = int(input())
for _ in range(R):
    lst = list(map(int, input().split()))

    result = []
    for item in lst[1:]:
        if pills.get(item, -1) == -1:
            print('YOU DIED')
            break
        result.append(pills[item])
    else:
        print(*result)
