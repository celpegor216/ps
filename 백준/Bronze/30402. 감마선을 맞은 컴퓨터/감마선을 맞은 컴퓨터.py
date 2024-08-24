N = 15
lst = [input() for _ in range(N)]

result = ''
for line in lst:
    if 'w' in line:
        result = 'chunbae'
    elif 'b' in line:
        result = 'nabi'
    elif 'g' in line:
        result = 'yeongcheol'
    
    if result:
        break

print(result)