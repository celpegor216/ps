A, B = map(int, input().split())

if A > B:
    A, B = B, A

print(B - A - 1 if B - A > 1 else 0)
print(*range(A + 1, B))