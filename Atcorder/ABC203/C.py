N, K = map(int, input().split())

L = [[] for i in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    L[i] = (a, b)

LL = sorted(L)

for i in range(N):
    if (LL[i][0] > K):
         break
    K += LL[i][1]

print(K)