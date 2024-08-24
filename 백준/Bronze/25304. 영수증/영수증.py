X = int(input())
N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    X -= A * B

print('Yes' if not X else 'No')