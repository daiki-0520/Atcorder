def change(a, b, p):
    for c in range(K):
        for d in range(K):
            if (a + b) == (c + d) or (a - b) == (c - d) or (abs(a - c) + abs(b - d)) <= 3:
                if grid[c][d] == -1:
                    grid[c][d] = p + 1


K = 41
grid = [[-1] * K for _ in range(K)]
grid[K // 2][K // 2] = 0

for i in range(10):
    for a in range(K):
        for b in range(K):
            if grid[a][b] == i:
                change(a, b, i)

for row in grid:
    print(*row)