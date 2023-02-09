while 1:
    try:
        s, t = input().split()

        sidx = 0
        tidx = 0
        while sidx < len(s) and tidx < len(t):
            if s[sidx] == t[tidx]:
                sidx += 1
                tidx += 1
            else:
                tidx += 1

        if sidx == len(s):
            print('Yes')
        else:
            print('No')

    except:
        break