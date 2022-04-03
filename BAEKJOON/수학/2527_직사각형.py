for i in range(4) :
  x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())

  #두 사각형 왼쪽x의 최대
  xt=max(x1,x2)
  #두사각형 오른쪽 x의 최소
  pt=min(p1,p2)
  #두사각형 아래쪽 y의 최대
  yt=max(y1,y2)
  #두사각형 위쪽 y의 최소 
  qt=min(q1,q2)

  #연산 
  xx=pt-xt
  yy=qt-yt

  #오른쪽 x의 최소에서 왼쪽 x의 최대를 뺀 값이 0보다 크고 
  #위쪽 y의 최소에서 아래쪽 y의 최대를 뺀 값이 0보다 크면 
  #사각형 겹치는 부분이 직사각형 
  if xx>0 and yy>0 :
    print('a')
  #0보다 작으면 겹치지 않음 
  elif xx<0 or yy<0 :
    print('d')
  #둘이 점으로 만남 
  elif xx==0 and yy==0 :
    print('c')
  #아니면 선분으로 만남 
  else :
    print('b')