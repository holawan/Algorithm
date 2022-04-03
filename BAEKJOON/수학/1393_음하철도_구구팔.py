stop_x,stop_y = map(int,input().split())
info = list(map(int,input().split()))

now_x,now_y = info[0],info[1]
dx,dy = info[2],info[3]

#dx와 dy가 둘다 정수범위에서 움직이기 때문에 최대공약수 계산 
def gcd(a,b) :
    if a>b :
        a,b = b,a 
    while b>0 :
        a,b = b, a%b
    return a

#최초 위치와 정류장의 거리 유클리드 게산
direct = [((stop_x-now_x)**2 + (stop_y-now_y)**2)**(1/2)]

#최대공약수 계산
my_gcd = gcd(dx,dy)
#이동거리 재정의
dx = dx//my_gcd
dy = dy//my_gcd

#반복문 시작 
while True :
    #현위치에서 dx,dy+
    now_x += dx
    now_y += dy
    #유클리드 거리 계산
    now = ((stop_x-now_x)**2 + (stop_y-now_y)**2)**(1/2)
    #현위치에서 유클리드 계산한 거리가 이전 위치에서 계산한 거리보다 크면 멈춤
    if now > direct[-1] :
        break
    else :
        direct.append(now)

print(now_x-dx,now_y-dy)
