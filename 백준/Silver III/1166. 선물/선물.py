# 이분탐색 같은데 실수는 어떻게 해야 하지?
# 해답: https://sophuu.tistory.com/50

N, L, W, H = map(int, input().split())

start, end = 0, max(L, W, H)

# 오차 범위를 줄이기 위해 while이 아닌 for 사용
# 반복 횟수는 충분히 크게 잡으면 됨
for _ in range(10000):
    middle = (start + end) / 2

    total = (L // middle) * (W // middle) * (H // middle)

    if total >= N:
        start = middle
    else:
        end = middle

print(f'{middle:0.10f}')