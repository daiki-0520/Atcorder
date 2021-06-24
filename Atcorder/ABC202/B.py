S = list(map(int, input()))

for i in range(len(S)):
    if S[i] == 6:
        S[i] = 9
    elif S[i] == 9:
        S[i] = 6
    else:
        S[i] = S[i]

T = [str(i) for i in S]
T.reverse()

A = ''.join(T)
print(A)