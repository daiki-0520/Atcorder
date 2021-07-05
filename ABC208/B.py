
a = 1
b = 2
c = 6
d = 24
e = 120
f = 720
g = 5040
h = 40320
i = 362880
j = 3628800


def main():
    ans = 0
    p = int(input())
    if p >= j:
        jj = p // j
        ans += jj
        p -= jj * j
        if p == 0:
            print(ans)
            return 

    if p < j and p >= i:
        ii = p // i
        ans += ii
        p -= ii * i
        if p == 0:
            print(ans)
            return 
    if p < i and p >= h:
        hh = p // h
        ans += p // h
        p -= hh * h
        if p == 0:
            print(ans)
            return 

    if p < h and p >= g:
        gg = p // g
        ans += p // g
        p -= gg * g
        if p == 0:
            print(ans)
            return 
     
    if p < g and p >= f:
        ff = p // f
        ans += p // f
        p -= ff * f
        if p == 0:
            print(ans)
            return 
    
    if p < f and p >= e:
        ee = p // e
        ans += p // e
        p -= ee * e
        if p == 0:
            print(ans)
            return 
    
    if p < e and p >= d:
        dd = p // d
        ans += p // d
        p -= dd * d
        if p == 0:
            print(ans)
            return 
    
    if p < d and p >= c:
        cc = p // c
        ans += p // c
        p -= cc * c
        if p == 0:
            print(ans)
            return 
   
    if p < c and p >= b:
        bb = p // b
        ans += p // b
        p -= bb * b
        if p == 0:
            print(ans)
            return
    
    if p < b and p >= a:
        aa = p // a
        ans += p // a
        p -= aa * a
        if p == 0:
            print(ans)
            return 
        
    if p < a and p >= 0:
        ans += p
        p -= p
        if p == 0:
            print(ans)
            return 
    print(ans)
    
if __name__ == '__main__':
    main()