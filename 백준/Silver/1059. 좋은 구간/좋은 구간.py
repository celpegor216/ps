L = int(input())
lst = sorted(map(int, input().split()))
N = int(input())

result = 0

if N not in lst:
    # minv: N보다 작은 것들 중 가장 큰 것(1~N)
    # maxv: N보다 큰 것들 중 가장 작은 것(N~1000)
    minv, maxv = 0, 1001

    for item in lst:
        if item < N and item > minv:
            minv = item
        if item > N and item < maxv:
            maxv = item
    
    minv += 1
    maxv -= 1
    
    for i in range(minv, N + 1):
        if i < N:
            result += maxv - N + 1
        else:
            result += maxv - i

print(result)