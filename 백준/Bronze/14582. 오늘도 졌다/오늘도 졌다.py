# 역전패가 성립하려면 경기 도중 울림 제미니스가 이기고 있는 순간이 있어야 한다
A = list(map(int, input().split()))
B = list(map(int, input().split()))

N = 9

a = b = 0
for n in range(N):
    a += A[n]

    if a > b:
        print('Yes')
        break
    
    b += B[n]
else:
    print('No')