n = int(input())
lst = [list(map(int,input().split())) for i in range(n)]
lst.sort(key = lambda x:x[1])
lst.sort(key = lambda x:x[0])

for num in lst :
  print(num[0],num[1])