A = list(map(int, input().split()))
B = sorted(A)

if  B[2] - B[1] == B[1] - B[0]:
    print("Yes") 
else:
    print("No")