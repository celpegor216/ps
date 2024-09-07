E, F, C = map(int, input().split())

result = 0
now = E + F
while now >= C:
    result += now // C
    now = now // C + now % C

print(result)