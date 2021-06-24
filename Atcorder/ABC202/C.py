from collections import Counter


N = int(input())
A = list(map(int, input().split()))
ans = 0

tmp = Counter(A)

l = []

for i in map(int, input().split()):
    l.append(tmp[i])

for i in map(int, input().split()):
    ans += l[i - 1]

print(ans)