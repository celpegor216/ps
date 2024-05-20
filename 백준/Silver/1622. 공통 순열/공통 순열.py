while 1:
    try:
        A = input()
        B = input()
        
        bucket_a = [0] * 26
        bucket_b = [0] * 26

        for a in A:
            bucket_a[ord(a) - ord('a')] += 1
        for b in B:
            bucket_b[ord(b) - ord('a')] += 1
        
        result = ''

        for i in range(26):
            result += chr(ord('a') + i) * min(bucket_a[i], bucket_b[i])

        print(result)
    except:
        break