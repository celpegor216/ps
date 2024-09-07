tc = 0

while 1:
    tc += 1
    
    a = input()
    b = input()

    if a == b == 'END':
        break

    bucket_a = [0] * 26
    bucket_b = [0] * 26

    for s in a:
        bucket_a[ord(s) - ord('a')] += 1
    for s in b:
        bucket_b[ord(s) - ord('a')] += 1
    
    for i in range(26):
        if bucket_a[i] != bucket_b[i]:
            print(f'Case {tc}: different')
            break
    else:
        print(f'Case {tc}: same')