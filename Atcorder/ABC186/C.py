N = int(input())
ans = 0
for i in range(1, N + 1):
    s_decimal = str(i)
    s_octal = format(i, 'o')
    if not('7' in s_decimal or '7' in s_octal):
        ans += 1
    

print(ans)