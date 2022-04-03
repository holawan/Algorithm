a,b,c,d,e=map(int,input().split())
#숫자를 다 받아오고 제곱 한후 더해준다. 그 후 10으로 나눠준다. 
print((a**2+b**2+c**2+d**2+e**2)%10)