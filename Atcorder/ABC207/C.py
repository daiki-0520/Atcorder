N = int(input())

a = [[] for i in range(N)]


for i in range(N):
    t, l, r = map(int, input().split())
    a[i] = [t, l, r]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if a[i][0] == 1:
            if a[i][1] == a[j][1]:
                ans += 1
            elif a[i][1] < a[j][1]:
                if a[i][2] >= a[j][1]:
                    ans += 1
            elif a[i][1] > a[j][1] and a[i][1] <= a[j][2]:
                ans += 1

        elif a[i][0] == 2:
            if a[i][1] == a[j][1]:
                ans += 1
            elif a[i][1] < a[j][1]:    
                if a[i][2] > a[j][1]:
                    ans += 1
            elif a[i][1] > a[j][1] and a[i][1] < a[j][2]:
                ans += 1
        elif a[i][0] == 3:
            if a[i][1] < a[j][1]:
                if a[i][2] >= a[j][1]:
                    ans += 1
            elif a[i][1] >= a[j][1] and a[i][1] <= a[j][2]:
                ans += 1

        elif a[i][0] == 4:
            if a[i][1] < a[j][1]:
                if a[i][2] > a[j][1]:
                    ans += 1
            elif a[i][1] > a[j][1] and a[i][1] < a[j][2]:
                ans += 1
    
print(ans)

            


