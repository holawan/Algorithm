

def dfs(n,p,m,t,d,result) :
    global my_min,my_max
    if n ==N :
        my_min = min(result,my_min)
        my_max = max(result,my_max)
        return
    #연산자가 있으면 해당 연산자로 계산하고 횟수 줄이기 
    if p :
        dfs(n+1,p-1,m,t,d,result+numbers[n])
    if m :
        dfs(n+1,p,m-1,t,d,result-numbers[n])
    if t :
        dfs(n+1,p,m,t-1,d,result*numbers[n])
    if d :
        dfs(n+1,p,m,t,d-1,int(result/numbers[n]))
        


N = int(input())

numbers = list(map(int,input().split()))
calc = list(map(int,input().split()))
my_min = 10e9
my_max = -10e9

dfs(1,calc[0],calc[1],calc[2],calc[3],numbers[0])
print(my_max)
print(my_min)



