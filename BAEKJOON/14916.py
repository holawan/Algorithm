n = int(input())

x=0
while n >0 :
	if n%5==0 :
		x += n//5
		break
	else :
		n -= 2
		x +=1 
if n < 0 :
	print(-1)
else :
	print(x)
	