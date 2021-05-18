def solve():
    alco = 0
    for i in range(1, N+1):
        v, p = map(int, input().split())
        alco += v * p
        if alco > 100 * x:
            return i
    return -1

n, x = map(int, input().split())

print(solve())