N = int(input())

result = 0

while N > 0:
    K = 1
    
    while N >= K:
        N -= K
        K += 1
        result += 1

print(result)