a, b, c, d = map(int, input().split())

if b >= c * d:
    print(-1)

else:
    e = 0
    f = 0
    i = 0
    n = 0
    while(n < 1000000):
        if a + e <= int(f * d):
            print(i)
            break
        e += b
        f += c
        i += 1
    
    else:
        print(-1)





