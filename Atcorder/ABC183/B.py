s1, s2, g1, g2 = map(int, input().split())


ans = (s1 * g2 + s2 * g1)/(g2 + s2)
print(ans)