# 해답: https://velog.io/@h33s00/15719-%EC%A4%91%EB%B3%B5%EB%90%9C-%EC%88%AB%EC%9E%90
# 입력을,,, sys.stdin.readline으로 받아서 처리해야 함


import sys

N = int(input())
lst = sys.stdin.readline()

total = 0
tmp = ''
for item in lst:
    if item.isdigit():
        tmp += item
    else:
        total += int(tmp)
        tmp = ''

print(total - ((N * (N - 1)) // 2))