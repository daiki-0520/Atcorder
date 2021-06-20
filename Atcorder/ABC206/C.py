N = int(input())
A = list(map(int, input().split()))
B = sorted(A)
B.append(0)
l = len(A)

proans = int(l * (l-1) / 2)
count = 1

for i in range(N):
    if B[i] == B[i + 1]:
        count += 1
    else:
        proans -= int(count * (count - 1) / 2)
        count = 1

print(proans)