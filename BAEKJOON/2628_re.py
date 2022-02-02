a,b = map(int,input().split()) 
num = int(input())
x = [a]
y = [b]
for i in range(num) :
    a,b = map(int,input().split())
    if a == 1 :
        x.append(b)
    else :
        y.append(b)

x.sort();y.sort()

m_x = x[0]
for i in range(1,len(x)) :
    if x[i]-x[i-1] > m_x :
        m_x =  x[i]-x[i-1]

m_y = y[0]
for i in range(1,len(y)) :
    if y[i]-y[i-1] > m_y :
        m_y =  y[i]-y[i-1]

print(m_x*m_y)