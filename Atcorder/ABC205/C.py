A, B, C = map(int, input().split())

a = abs(A)
b = abs(B)

if C % 2 == 0:
    if a < b:
        print("<")
    elif a == b:
        print("=")
    else:
        print(">")
else:
    if A < B:
        print("<")
    elif A == B:
        print("=")
    else:
        print(">")