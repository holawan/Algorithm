import sys
a,b = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

result = []
for i in range((a-b)+1):
    result.append(sum(lst[i:i+b]))
print(max(result))