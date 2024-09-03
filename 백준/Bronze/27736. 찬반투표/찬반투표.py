# 해당 투표에서 찬성이 반대보다 많으면 투표가 통과된다.
# 반대가 찬성보다 많거나, 반대와 찬성의 수가 동일하다면 투표는 통과되지 않는다.
# 단, 기권한 사람이 재학생의 절반 이상이라면 찬성과 반대의 수와 관계없이 항상 투표는 무효 처리된다.

N = int(input())
lst = list(map(int, input().split()))

a = lst.count(1)
r = lst.count(-1)
i = lst.count(0)

if i >= (N + 1) // 2:
    print('INVALID')
elif a > r:
    print('APPROVED')
else:
    print('REJECTED')