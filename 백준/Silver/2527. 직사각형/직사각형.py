for i in range(4):
    ax, ay, ap, aq, bx, by, bp, bq = list(map(int, input().split()))

    a_dots = [(ax, ay), (ap, ay), (ax, aq), (ap, aq)]
    b_dots = [(bx, by), (bp, by), (bx, bq), (bp, bq)]

    result = 'a'

    if ax > bp or ap < bx or ay > bq or aq < by:
        result = 'd'
    elif a_dots[0] == b_dots[3] or a_dots[1] == b_dots[2] or a_dots[2] == b_dots[1] or a_dots[3] == b_dots[0]:
        result = 'c'
    elif ((ay == bq or by == aq) and not(ax > bp or ap < bx)) or ((ax == bp or bx == ap) and not(ay > bq or aq < by)):
        result = 'b'

    print(result)