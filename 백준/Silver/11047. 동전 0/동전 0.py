N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]

result = 0
while K:
    result += K // lst[-1]
    K %= lst[-1]
    lst.pop()

print(result)