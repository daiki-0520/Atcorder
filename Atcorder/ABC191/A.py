V,T,S,D = map(int,input().split())

if V*T > D or D > V*S:
    print('Yes')
else:
    print('No')