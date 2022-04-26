n= int(input())

l,r = 3,7
if n == 1 :
    result = 3 
else :
    result = 7
for i in range(2,n) :
    result = l+r*2 
    l ,r = r,result

print(result%9901)