x, y = map(int, input().split())

d = max(x,y) - min(x,y)

if d < 3:
    print('Yes')
else:
    print('No')