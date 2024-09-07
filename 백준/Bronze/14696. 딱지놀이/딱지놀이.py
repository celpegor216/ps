N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    bucket_A = [0] * 5
    bucket_B = [0] * 5

    for i in range(A[0]):
        bucket_A[A[i + 1]] += 1
    for i in range(B[0]):
        bucket_B[B[i + 1]] += 1
    
    for i in range(4, 0, -1):
        if bucket_A[i] > bucket_B[i]:
            print('A')
            break
        elif bucket_A[i] < bucket_B[i]:
            print('B')
            break
    else:
        print('D')