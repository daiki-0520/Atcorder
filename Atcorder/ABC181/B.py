def calc(x):
    return x * (x + 1) // 2

n = int(input())

ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    ans += (calc(b) - calc(a - 1))

print(ans)
