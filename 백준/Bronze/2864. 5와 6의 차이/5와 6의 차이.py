A, B = input().split()

maxA = int(A.replace('5', '6'))
maxB = int(B.replace('5', '6'))
minA = int(A.replace('6', '5'))
minB = int(B.replace('6', '5'))

print(minA + minB, maxA + maxB)