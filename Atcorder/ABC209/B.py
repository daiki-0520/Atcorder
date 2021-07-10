n, x = map(int, input().split())

c = list(map(int, input().split()))

a = []
b = []

for i in range(len(c)):
    if i % 2 == 0:
        a.append(c[i])
    else:
        b.append(c[i])


for i in range(len(b)):
    b[i] -= 1

d = sum(a) + sum (b)

if x >= d:
    print('Yes')
else:
    print('No')
