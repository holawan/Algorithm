a,b = map(int,input().split())

c = a*60 + b

x = list(divmod((c-45),60))
if x[0] <0 :
    x[0] += 24
print(x[0], x[1])