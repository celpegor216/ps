X, Y = input().split()

def rev(num):
    return int(num[::-1])

print(rev(str(rev(X) + rev(Y))))