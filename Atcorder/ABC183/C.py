from intertools import permutations

N, K = map(int, input().split())

T = [list(map(int, input().split()) for _ in range(N))]

ans = 0

for per in permutations(range(1, N)):
    time = 0
    prev = 0
    for i in range(N-1):
        score += T[prev][per[i]]
        prev = per[i]
    score +=T[prev][0]

    if score == K:
        ans += 1

print(ans)


    
        



