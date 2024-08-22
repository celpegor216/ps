while 1:
    try:
        N = input()
        result = len(N)
        N = int(N)

        while 1:
            if not int('1' * result) % N:
                break
            result += 1

        print(result)
    except:
        break