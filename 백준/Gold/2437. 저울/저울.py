# 브루트포스밖에 방법이 생각나지 않음...
# 해답: https://seongonion.tistory.com/127

N = int(input())
lst = sorted(map(int, input().split()))
lst.sort()

# 구할 수 있는 구간의 끝
end = 0

for n in range(N):
    # 구간이 겹치거나 연속되는지 확인
    if lst[n] <= end + 1:
        end += lst[n]
    else:
        break

print(end + 1)