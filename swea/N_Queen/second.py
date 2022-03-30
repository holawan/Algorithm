
n = int(input())
ans = 0
row = [300] * n



def queen(x,n):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # 퀸 놓기 
            row[x] = i
            
            for j in range(x) :

                if row[j] == row[x] or abs(row[x]-x) == (row[j]-j) :
                    break 
            else :
                queen(x+1,n)

queen(0,n)
print(ans)