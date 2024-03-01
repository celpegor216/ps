s = input()

length = len(s)
N = 0

if length > 9:
    tmp = length - 9
    N = 9 + tmp // 2
else:
    N = length

used = [0] * (N + 1)
result = []

def find(idx, lst):
    global result

    if idx >= length:
        result = lst[:]
        return
    
    if result:
        return
    
    one = int(s[idx:idx + 1])
    if one <= N and not used[one]:
        used[one] = 1
        find(idx + 1, lst + [one])
        used[one] = 0
    
    two = int(s[idx:idx + 2])
    if two <= N and not used[two]:
        used[two] = 1
        find(idx + 2, lst + [two])
        used[two] = 0

find(0, [])

print(*result)