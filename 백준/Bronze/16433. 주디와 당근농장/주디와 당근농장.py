N, R, C = map(int, input().split())

lines = ['v.' * (N // 2) + ('v' if N % 2 else ''), '.v' * (N // 2) + ('.' if N % 2 else '')]

if (R % 2 and C % 2) or (not R % 2 and not C % 2):
    for n in range(N):
        print(lines[n % 2])
else:
    for n in range(N):
        print(lines[(n + 1) % 2])