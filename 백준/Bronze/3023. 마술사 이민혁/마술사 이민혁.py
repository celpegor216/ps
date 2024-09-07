N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
A, B = map(int, input().split())

result = []
for n in range(N):
    result.append(lst[n] + lst[n][::-1])

for n in range(N - 1, -1, -1):
    result.append(result[n][:])

result[A - 1][B - 1] = '.' if result[A - 1][B - 1] == '#' else '#'

for line in result:
    print(''.join(line))