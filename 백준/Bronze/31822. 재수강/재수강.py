TARGET = input()
N = int(input())

result = 0
for _ in range(N):
    S = input()
    if S[:5] == TARGET[:5]:
        result += 1

print(result)