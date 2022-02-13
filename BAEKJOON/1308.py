y1,m1,d1 = map(int,input().split())
y2,m2,d2 = map(int,input().split())

# def yoon(year) :
#     return year//4-year//10+year//400

# def mon(year,month) :
#     if month == 0 :
#         return 0
#     result = 0
#     for i in range(1,month+1) :
#         if i in [1,3,5,7,8,10,12] :
#             result += 31
#         elif i in [4,6,9,11] :
#             result += 30
#         elif i == 2 :
#             if year//400 == 0:
#                 result += 29
#             elif year//100 ==0 :
#                 result += 28
#             elif year//4 ==0 :
#                 result += 29
#             else :
#                 result += 28
#     return result



# Day1 = (y1-1)*365+yoon(y1-1) + mon(y1,m1-1) + d1
# Day2 = (y2-1)*365+yoon(y2-1) + mon(y2,m2-1) + d2

# if y2-y1>1000 :
#     print('gg')
#     exit()
# elif y2-y1==1000 and m2>m1 :
#     print('gg')
#     exit()
# elif y2-y1==1000 and m1==m2 and d2>=d1 :
#     print('gg')
#     exit()
# else : 
#     print(f'D-{Day2-Day1}')
import datetime


d_day = int(str(datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).split()[0])

over = 0 
for i in range(0,1000) :
    if i%400==0 :
        over +=366
    elif i%100==0 :
        over += 365
    elif i%4==0 :
        over += 366
    else :
        over += 365

if d_day >= over :
    print('gg')
else :
    print(f'D-{d_day}')
