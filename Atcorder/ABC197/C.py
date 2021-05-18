def solve():
    from itertools import product

    N = int(input())
    A = [*map(int, input().split())]
    ans = float('INF')

    for bit in product((True, False), repeat=N-1):
        score = 0
        cur = 0

        for i in range(N-1):
            cur |= A[i]
            if bit[i]:
                score ^= cur
                cur = 0
        cur |= A[N-1]
        score ^= cur

        ans = min(ans, score)

    print(ans)

solve()