A1, A0 = map(int, input().split())
C = int(input())
N0 = int(input())

print(1 if A1 <= C and A1 * N0 + A0 <= C * N0 else 0)