N = int(input())
M = 26

for _ in range(N):
    A, B = input().split()

    bucket_A = [0] * M
    bucket_B = [0] * M

    for a in A:
        bucket_A[ord(a) - ord('a')] += 1
    
    for b in B:
        bucket_B[ord(b) - ord('a')] += 1
    
    for m in range(M):
        if bucket_A[m] != bucket_B[m]:
            print('Impossible')
            break
    else:
        print('Possible')