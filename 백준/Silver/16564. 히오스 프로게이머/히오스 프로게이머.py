import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = []

start = 1
end = 10 ** 20

for n in range(N):
    num = int(input())

    lst.append(num)

    if num < start:
        start = num

result = start
while start <= end:
    middle = (start + end) // 2

    total = 0
    for n in range(N):
        if lst[n] < middle:
            total += middle - lst[n]
    
    if total <= K:
        result = max(result, middle)
        start = middle + 1
    else:
        end = middle - 1

print(result)