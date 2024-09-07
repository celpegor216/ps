N = 10
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = b = 0
for n in range(N):
    if A[n] > B[n]:
        a += 1
    elif A[n] < B[n]:
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('D')