T = int(input())

for t in range(1,T+1) :
    n = int(input())
    line = input()
    cnt = 0
    max_cnt = 0
    for s in line :
        if s == '1' :
            cnt +=1
        else :
            cnt = 0
        if cnt > max_cnt :
            max_cnt = cnt
    print(f'#{t} {max_cnt}')

