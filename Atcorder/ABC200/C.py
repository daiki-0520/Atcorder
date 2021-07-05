n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 200
for i in a:
    cnt[i % 200] += 1
cnt = [c * (c - 1) / 2 for c in cnt]
print(int(sum(cnt)))