# 힌트: 진짜로 뒤집으면 안 된다

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    p = input()    # 수행할 함수들
    n = int(input())    # 배열에 들어있는 수의 개수
    lst = input().strip()    # 배열

    # 원소가 하나도 없는 경우
    if n == 0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
    # 원소가 하나라도 있는 경우
    else:
        lst = list(map(int, lst[1:-1].split(',')))

        pointer = 0

        result = ''

        for command in p:
            if command == 'R':
                if pointer == 0:
                    pointer = -1
                else:
                    pointer = 0
            elif command == 'D':
                if len(lst) < 1:
                    result = 'error'
                    break
                else:
                    lst.pop(pointer)

        if result != 'error':

            if pointer == -1:
                lst.reverse()

            print('[', end='')
            for i in range(len(lst)):
                if i != len(lst) - 1:
                    print(lst[i], end=',')
                else:
                    print(lst[i], end='')
            print(']')
        else:
            print(result)