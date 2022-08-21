S = input()

x = S.split('0')
y = S.split('1')
x_cnt = 0
y_cnt = 0

for _ in x :
    if _ != '' :
        x_cnt+=1 

for _ in y :
    if _ != '' :
        y_cnt += 1 

print(min(x_cnt,y_cnt))