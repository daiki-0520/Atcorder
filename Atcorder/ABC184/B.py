N, X = map(int, input().split())
ans = input()

for i in range(N):
    if ans[i] == 'o':
        x += 1
    else:
        if X == 0:
            continue
        else:
            X -= 1

print(X)