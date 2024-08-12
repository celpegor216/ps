N = int(input())
queries = []

for _ in range(N):
    num, s, b = map(int, input().split())
    num = str(num)
    queries.append((num, s, b))

result = 0

# 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수
for i in range(123, 988):
    st = str(i)
    if '0' in st or st[0] == st[1] or st[1] == st[2] or st[0] == st[2]:
        continue

    for num, s, b in queries:
        cnt_s = cnt_b = 0
        for j in range(3):
            if st[j] == num[j]:
                cnt_s += 1
            elif st[j] in num:
                cnt_b += 1
        if cnt_s != s or cnt_b != b:
            break
    else:
        result += 1

print(result)