n = int(input())

ans = 0

if n % 100 == 0: 
    ans = int(n / 100)
else:
    ans = n // 100 + 1 

print(ans)