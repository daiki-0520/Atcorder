S = input()

if len(S) == 1:
    if S.islower():
        print('Yes')
    else:
        print('No')

else:
    A = S[::2]
    B = S[1::2]

    if A.islower() and B.isupper():
        print('Yes')
    else:
        print('No')