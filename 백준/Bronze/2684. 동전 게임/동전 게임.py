T = int(input())

for _ in range(T):
    S = input().replace('H', '1').replace('T', '0')
    bucket = [0] * 8
    
    for i in range(38):
        bucket[int(S[i:i + 3], 2)] += 1
    
    print(*bucket)