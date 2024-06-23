N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

result_t = 0

for size in sizes:
    result_t += size // T
    if size % T:
        result_t += 1

print(result_t)
print(N // P, N % P)