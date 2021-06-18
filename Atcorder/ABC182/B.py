N = int(input())
a = list(map(int, input().split()))

result = 0
for i in range(2 , 1000):
    t = 0
    for x in a:
        if x % i == 0:
            t += 1
    result = max(result, t)

print(result)

