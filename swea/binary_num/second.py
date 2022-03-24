T = int(input())
for t in range(1,T+1) :
    n = float(input())
    ans = ''
    binary_num = [0]*12

    cnt = 0
    while cnt < 12 and n>0:
        binary_num[cnt] = str(int(n*2))
        n = n*2-int(n*2)
        cnt += 1 
    if n>0 :
        print(f'#{t} overflow')
    else :
        print(f'#{t} {"".join(binary_num[:cnt])}')
