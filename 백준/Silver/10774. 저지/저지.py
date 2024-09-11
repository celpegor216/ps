N = int(input())
M = int(input())
sizes = [input() for _ in range(N)]

size_to_num = {'S': 0, 'M': 1, 'L': 2}

# 요구하는 번호가 맞고 사이즈는 같거나 그 이상
used = [0] * N

for _ in range(M):
    size, number = input().split()
    number = int(number) - 1

    if not used[number] and size_to_num[sizes[number]] >= size_to_num[size]:
        used[number] = 1

print(sum(used))