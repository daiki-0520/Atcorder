n = int(input())
A = []
B = []

for _ in range(n):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

and = float('INF')

for i in range(N):
    for j in range(N):
        if i == j:
            score = A[i] + B[i]
        else:
            score = max(A[i], B[i])
        ans = min(ans, score)

print(ans)