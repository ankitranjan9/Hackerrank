n = int(input())
S = set(map(int, input().split()))
tot = 0
for i in S:
  tot += i


print(tot/len(S))
