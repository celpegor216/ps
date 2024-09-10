N = int(input())
nums = list(map(int, input().split()))
S = input()

bucket = [0] * 53

for num in nums:
    bucket[num] += 1

for s in S:
    if s == ' ' and bucket[0]:
        bucket[0] -= 1
    elif s.isupper() and bucket[1 + ord(s) - ord('A')]:
        bucket[1 + ord(s) - ord('A')] -= 1
    elif s.islower() and bucket[27 + ord(s) - ord('a')]:
        bucket[27 + ord(s) - ord('a')] -= 1
    else:
        print('n')
        break
else:
    print('y')