x = 1000 - int(input())

money = 0
if x//500 >0 :
    money += x//500
    x -= 500*(x//500)
if x //100 >0 :
    money += x//100
    x -= 100*(x//100)
if x //50 >0 :
    money += x//50 
    x -= 50 *(x//50)
if x//10 >0 :
    money += x//10 
    x -= 10*(x//10)
if x//5 >0 :
    money += x//5 
    x -= 5*(x//5)
if x>0 :
    money += x
print(money)