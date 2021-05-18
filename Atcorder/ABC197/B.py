H,W,X,Y = map(int, input().split())
X -= 1
Y -= 1
grid = []

for _ in range(H):
    s = input()
    grid.append(s)

ans = 1

for row in reversed(range(X)):
    if grid[row][Y] == "#":
        break
    else:
        ans += 1

for row  in range(X + 1, H):
    if grid[row][Y] == "#":
        break
    else:
        ans += 1

for col in reversed(range(Y)):
    if grid[X][col] == "#":
        break
    else:
        ans += 1
    
for col in range(Y + 1, W):
    if grid[X][col] == "#":
        break
    else:
        ans += 1

print(ans)
