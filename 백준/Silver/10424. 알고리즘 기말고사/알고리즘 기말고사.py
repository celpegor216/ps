N = int(input())
lst = [0] + list(map(int, input().split()))
new_lst = [0] * (N + 1)
for i in range(1, N + 1):
    new_lst[lst[i]] = i
# lst[i]: 중간고사 성적이 i등이고, 기말고사 성적이 lst[i]등
lst = new_lst

for i in range(1, N + 1):
    print(i - lst[i])