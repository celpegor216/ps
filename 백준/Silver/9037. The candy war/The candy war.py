T = int(input())

# 정답을 찾았을 때 바로 종료하기 위해 함수 사용
def find():
    N = int(input())
    lst = list(map(int, input().split()))

    # 최초 짝수 보충
    for n in range(N):
        if lst[n] % 2:
            lst[n] += 1

    result = 0
    while 1:
        # 모두 같은 개수를 가지고 있는지 확인
        for n in range(1, N):
            if lst[n] != lst[0]:
                break
        else:
            return result

        # 분배
        new_lst = [item // 2 for item in lst]
        for n in range(N):
            new_lst[(n + 1) % N] += lst[n] // 2

        lst = new_lst

        # 짝수 보충
        for n in range(N):
            if lst[n] % 2:
                lst[n] += 1

        result += 1

for _ in range(T):
    print(find())
