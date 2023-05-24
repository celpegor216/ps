E, S, M = map(int, input().split())

for i in range(1, 15 * 28 * 19 + 1):
    e = i % 15 if i % 15 else 15
    s = i % 28 if i % 28 else 28
    m = i % 19 if i % 19 else 19
    
    if e == E and s == S and m == M:
        print(i)
        break