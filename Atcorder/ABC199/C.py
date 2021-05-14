def get_index(x):
    if x < N:
        return 0, x
    else:
        return 1, x-N

N = int(input())
S = input()
first = list(S[:N])
second = list(S[N:])
L = [first, second]

Q = int(input())
for _ in range(Q):
    t,a,b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        ai,aj = get_index(a)
        bi,bj = get_index(b)
        L[ai][aj], L[bi][bj] = L[bi][bj], L[ai][aj]
    else:
        L[0],L[1] = L[1],L[0]
    
    ans = ''.join(L[0]) + ''.join(L[1])
    print(ans)