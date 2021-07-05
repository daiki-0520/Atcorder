from math import factorial

p = int(input())
answer = 0

for i in range(1, 11):
    divisor = factorial(i + 1)
    print('divisor: ' + str(divisor))
    residue = p % divisor
    print('residue :' + str(residue))
    answer += residue // factorial(i)
    p -= residue

print(answer)