def check():
    for _ in range(N):
        x,y = map(int, input().split())
        if x < S and y > D:
            return True
    return false

n,s,d = map(int, input().split())
print('Yes' if solve() else 'No')