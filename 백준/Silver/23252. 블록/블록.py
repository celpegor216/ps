T = int(input())

def check(a, b, c):
    result = 'No'

    # ㄴ자 블록이 1칸 블록보다 많은 경우
    if a < c:
        return result

    # ㄴ자 블록과 1칸 블록의 수가 같은데,
    # 2칸 블록이 원래 홀수 개 있는데 끼워 넣고도 홀수 개가 남는 경우
    elif a == c:
        if b > c == 0 and b % 2:
            return result

    # ㄴ자 블록보다 1칸 블록이 많은데,
    # ㄴ자 블록에 들어칸 1칸 블록을 제외하고 1칸 블록이 홀수 개로 남는 경우
    else:
        if (a - c) % 2:
            return result

    return 'Yes'

for _ in range(T):
    a, b, c = map(int, input().split())

    print(check(a, b, c))