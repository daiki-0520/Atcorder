A, B, _W = map(int, input().split())
W = 1000 * _W

mn = float('inf')
mx = -1

for n in range(1, 10**6 + 1):
    l = A * n
    r = B * n
    if l <= W <= r:
        mn = min(mn, n)
        mx = max(mx, n)

if mx == -1:
    print('UNSATISFIABLE')
else:
    print(mn, mx)