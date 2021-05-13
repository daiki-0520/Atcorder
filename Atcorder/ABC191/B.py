n,x = map(int, input().split())
A = [*map(int, input().split())]
ans = []

for i in A:
    if i!= x:
        ans.append(i)

print(*ans)