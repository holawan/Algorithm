a,b = map(int,input().split())

#분단위로 바꿔주기 
c = a*60 + b

#45를 빼고 60으로 나누기 
x = list(divmod((c-45),60))

#몫이 0보다 작으면 24를 더해준다. 
if x[0] <0 :
    x[0] += 24
print(x[0], x[1])