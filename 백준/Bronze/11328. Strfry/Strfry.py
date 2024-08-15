T = int(input())

for _ in range(T):
    a, b = input().split()

    bucket_a = [0] * 26
    bucket_b = [0] * 26

    for s in a:
        bucket_a[ord(s) - ord('a')] += 1
    for s in b:
        bucket_b[ord(s) - ord('a')] += 1
    
    result = 1
    for i in range(26):
        if bucket_a[i] != bucket_b[i]:
            result = 0
            break
    
    print('Possible' if result else 'Impossible')