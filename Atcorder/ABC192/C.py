def calc(x):
    s = str(x)
    g1 = int("".join(sorted(s, reverse = True)))
    g2 = int("".join(sorted(s)))
    return g1-g2

N,K = map(int, input().split())

ans = N
for _ in range(K):
    ans = calc(ans)

print(ans)