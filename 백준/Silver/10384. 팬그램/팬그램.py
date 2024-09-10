T = int(input())

for t in range(T):
    S = input().lower()
    bucket = [0] * 26

    for s in S:
        if s.islower():
            bucket[ord(s) - ord('a')] += 1

    result = min(bucket)

    if not result:
        result = 'Not a pangram'
    elif result == 1:
        result = 'Pangram!'
    elif result == 2:
        result = 'Double pangram!!'
    elif result == 3:
        result = 'Triple pangram!!!'

    print(f'Case {t + 1}: {result}')