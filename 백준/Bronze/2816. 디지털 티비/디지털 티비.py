# 최소 횟수의 방법을 찾는 게 아니고 전체 채널이 최대 100개까지 주어지기 때문에
# KBS1을 먼저 찾아서 올리고 그 다음 KBS2를 찾아서 올려도 된다

N = int(input())
lst = [input() for _ in range(N)]

first = 'KBS1'
second = 'KBS2'

result = ''
if lst[0] != first:
    first_idx = lst.index(first)
    result += '1' * first_idx
    result += '4' * first_idx
    # KBS1 맨 위로 끌어올리기
    lst = [first] + lst[:first_idx] + lst[first_idx + 1:]

if lst[1] != second:
    second_idx = lst.index(second)
    result += '1' * second_idx
    result += '4' * (second_idx - 1)

print(result)