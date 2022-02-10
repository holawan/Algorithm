A,B,V = map(int,input().split())
#A는 올라감 B는 내려감 V는 막대 

# i = 0
# height =0
# while True :
#     i += 1 
#     height +=A 
#     if height >= V :
#         break
#     height -= B

# print(i)
import math
x = (V-A)/(A-B)
print(math.ceil(x)+1)