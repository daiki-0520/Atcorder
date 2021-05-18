def solve():
    count = 0
    i = 1
    while True:
        s = str(i) * 2
        x = int(s)
        if x < N:
            count += 1
        else:
            break
        i += 1
    return count

N = int(input())
print(solve())