N = list(map(int, input()))
b = len(N)
A = [0] * b
for i in range(b):
    A[i] = N[i] % 3

x = sum(A)

if x % 3 == 0:
    print(0)

elif x % 3 == 1:
    if 1 in A:
        if b <= 1:
            print(-1)
        else:
            print(1)
    else:
        if b <= 2:
            print(-1)
        else:
            print(2)
else:
    if 2 in A:
        if b <= 1:
            print(-1)
        else:
            print(1)
    else:
        if b <= 2:
            print(-1)
        else:
            print(2)
