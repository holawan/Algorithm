# import sys
#
# w, h = map(int, sys.stdin.readline().split())
# x, y = map(int, sys.stdin.readline().split())
# t = int(sys.stdin.readline())

# lst = [0,0,w,h]
#
# dx,dy = 'p','p'
# for i in range(t) :
#
#     if (x==w and y==h) or y==h:
#         dx,dy='m','m'
#     elif (x==0 and y==0) or x==0:
#         dx,dy = 'p','p'
#     elif x== w  or y==0:
#         dx,dy = 'm','p'
#     if dx == 'p':
#         x+=1
#     else :
#         x-=1
#     if dy == 'p':
#         y+=1
#     else :
#         y-=1
# print(x,y)
# x_direction = 'p'
# y_direction = 'm'
# while t >0 :
#     if x == w :
#         x_direction = 'm'
#     if x== 0 :
#         x_direction = 'p'
#     if y == h :
#         y_direction = 'm'
#     if y == 0 :
#         y_direction = 'p'
#     if x_direction == 'p' :
#         x += 1
#     else :
#         x-= 1
#     if y_direction == 'p' :
#         y+=1
#     else :
#         y-=1
#     t -=1
# print(x,y)


import sys

w, h = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())
lst = [] #가로 축 리스트
for i in range(0,w+1) :
    lst.append(i)

lst2 = [] #세로 축 리스트
for j in range(0,h+1) :
    lst2.append(j)

#t+x는 가로 축 총 이동거리
#t+y = 세로 축 총 이동거리
if (t+x)//w %2 : # 이동거리를 범위로 나눈 값이 홀수면
    res1 = -((t+x)%w)-1 #이동거리를 범위로 나눈 나머지에 -1한 값을 리턴
else :
    res1 = (t+x)%w      #이동거리를 범위로 나눈 값이 짝수면 이동거리를 범위로 나눈 나머지를 리턴

if (t+y)//h %2 :        # 이동거리를 범위로 나눈 값이 홀수면
    res2 =  -((t+y)%h)-1#이동거리를 범위로 나눈 나머지에 -1한 값을 리턴
else :
    res2 = (t+y)%h      #이동거리를 범위로 나눈 값이 짝수면 이동거리를 범위로 나눈 나머지를 리턴
#리스트에서 인덱스를 찾아 리턴
print(lst[res1],lst2[res2])

#이렇게 해결한 이유
## 개미는 가로축으로 012343210123 이런식으로 이동하고 세로축도 마찬가지로 번갈아가면서 이동한다.
##리스트를 앞으로 뒤로 순회하면 되는데, 몫이 짝수이면 나머지를 인덱스로 값을 구하고,
# 몫이 홀수이면 나머지를 음수로 변환하고, 나머지에 -1 한 값을 인덱스로 값을 구한다.
# [0,1,2,3,4]이 가로축이라고 가정하면,
# 2번 이동했을 때는 2(4%2=2, 4//2 =0), => lst[2] = 2
# 5번 이동했을 때는 3이다. (4%5 = 1, 4//5 = 1) => -1-1 = lst[-2] =3
