N = int(input())
S = input()

result = 1
idx = 0
while idx < N:
    if S[idx] == 'S':
        idx += 1
    else:
        idx += 2
    result += 1

print(min(result, N))