N = int(input())
A = list(map(int, input().split()))
AA = sorted(A)
B = [n for n in range(1, N + 1)]

if AA == B:
    print("Yes")
else:
    print("No")