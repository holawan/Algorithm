n = int(input())

grid = [list(map(int,input().split())) for _ in range(n)]

r,c = n//2,n//2

dr = [0,1,0,-1]
dc = [-1,0,1,0]

l = 1 
d = -1
cnt = 1 

out = 0 
left = 0
while 0<=r<n and 0<=c<n  :
    d += 1 
    l = d//2 +1

    for _ in range(l) :

        left = 0
        nr = r + dr[d%4] 
        nc = c + dc[d%4]  
        if nc == -1 :
            c = nc 
            break

        now = grid[nr][nc]

        #7%
        for k in [1,-1] :
            nnr = nr + dr[(d+k)%4]
            nnc=  nc + dc[(d+k)%4]
            if 0<= nnr <n and 0<=nnc<n :
                grid[nnr][nnc] += int(now*0.07)
            else :
                out += int(now*0.07)
            left += int(now*0.07)

        #2%
        for k in [1,-1] :
            nnr = nr + dr[(d+k)%4] *2
            nnc=  nc + dc[(d+k)%4] *2
            if 0<= nnr <n and 0<=nnc<n :
                grid[nnr][nnc] += int(now*0.02)
            else :
                out += int(now*0.02)
            left += int(now*0.02)


        #1%
        for k in [1,-1] :
            nnr = r + dr[(d+k)%4] 
            nnc=  c + dc[(d+k)%4] 
            if 0<= nnr <n and 0<=nnc<n :
                grid[nnr][nnc] += int(now*0.01)
            else :
                out += int(now*0.01)
            left += int(now*0.01)



        #10%
        nnr = nr + dr[d%4]
        nnc = nc + dc[d%4]
        for k in [1,-1] :
            nnnr = nnr + dr[(d+k)%4] 
            nnnc=  nnc + dc[(d+k)%4] 
            if 0<= nnnr <n and 0<=nnnc<n :
                grid[nnnr][nnnc] += int(now*0.1)
            else :
                out += int(now*0.1)
            left += int(now*0.1)


        #5%
        nnr = nr + dr[d%4] *3
        nnc = nc + dc[d%4] *3

        if 0<= nnr <n and 0<=nnc<n :
            grid[nnr][nnc] += int(now*0.05)
        else :
            out += int(now*0.05)
        left += int(now*0.05)

        # alpha
        nnr = nr + dr[d%4]
        nnc = nc + dc[d%4]
    
        if 0 <= nnr < n and 0 <= nnc < n:
            grid[nnr][nnc] += grid[nr][nc] - left
        else:
            out += grid[nr][nc] - left        

        r = nr 
        c = nc  

    

print(out)