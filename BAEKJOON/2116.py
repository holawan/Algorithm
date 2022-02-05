import sys

a,b = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))


M = []
M.append(sum(lst[0:b]))

for i in range((a-b)):
    S = M[i]-lst[i]+lst[i+b]
    M.append(S)
print(max(M))
