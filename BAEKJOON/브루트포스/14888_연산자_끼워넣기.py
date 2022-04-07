# def dfs(n,p,m,t,d,result) :
#     global my_min,my_max
#     if n ==N :
#         my_min = min(result,my_min)
#         my_max = max(result,my_max)
#         return
#     #연산자가 있으면 해당 연산자로 계산하고 횟수 줄이기 
#     if p :
#         dfs(n+1,p-1,m,t,d,result+numbers[n])
#     if m :
#         dfs(n+1,p,m-1,t,d,result-numbers[n])
#     if t :
#         dfs(n+1,p,m,t-1,d,result*numbers[n])
#     if d :
#         dfs(n+1,p,m,t,d-1,int(result/numbers[n]))
        


# N = int(input())

# numbers = list(map(int,input().split()))
# calc = list(map(int,input().split()))
# my_min = 10e9
# my_max = -10e9

# dfs(1,calc[0],calc[1],calc[2],calc[3],numbers[0])
# print(my_max)
# print(my_min)


from itertools import  permutations,product

def minimum(num,real_sub) :
    global my_min,my_max
    for sub in real_sub :
        result = num[0]
        for i in range(N-1) :
            if int(result)<0 and sub[i] == '//' and int(num[i+1])>0 :
                result = -(-int(result)//int(num[i+1]))
            else :
                result = eval(str(result)+sub[i]+num[i+1])

        if result < my_min :
            my_min = result
        if result > my_max :
            my_max = result
        

N = int(input())

numbers = list(input().split())
calc = list(map(int,input().split()))
real = []
for _ in range(calc[0]) :
    real.append('+')
for _ in range(calc[1]) :
    real.append('-')
for _ in range(calc[2]) :
    real.append('*')

for _ in range(calc[3]) :
    real.append('//')
real = [1,1,1,1]
real_sub = list(permutations(real,len(real)))
real_sub2 = list(product(real,len(real)))
print(real_sub)
print(real_sub2)
# print(real_sub)
my_min = 10e9
my_max = -10e9
minimum(numbers,set(real_sub))
print(my_max)
print(my_min)
