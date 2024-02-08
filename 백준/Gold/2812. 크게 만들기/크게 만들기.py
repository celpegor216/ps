# 시간 초과
# 해답: https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-2812%EB%B2%88-%ED%81%AC%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0

N, K = map(int, input().split())
nums = input()

stack = []

for num in nums:
    # 현재 숫자가 stack에 있는 숫자보다 크고, 지울 수 있는 기회가 남아있다면
    # stack에 있는 숫자를 지우고 현재 숫자를 넣음
    while stack and stack[-1] < num and K > 0:
        stack.pop()
        K -= 1
    stack.append(num)

# 지울 수 있는 기회를 다 쓰지 않았다면 뒤를 자름
if K > 0:
    print(''.join(stack[:-K]))
else:
    print(''.join(stack))