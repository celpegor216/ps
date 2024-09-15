M, N = map(int, input().split())
x, y = map(int, input().split())
T = int(input())

# T 최대가 21e8이네,,,^^

nx = (x + T) % (M * 2)
ny = (y + T) % (N * 2)

if nx > M:
    nx = M * 2 - nx

if ny > N:
    ny = N * 2 - ny

print(nx, ny)