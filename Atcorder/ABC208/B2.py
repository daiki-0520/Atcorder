from math import facrotial

p = int(input())
answer = 0
for i in range(10, 0, -1):
    while factorial(i) <= p:
        answer += 1
        p -= factorial(i)

print(answer)