# N,K = map(int,input().split())
# #N = int(input())
# def func(x) :
#     if x == 1 :
#         return 1 
#     else : 
#         return x*func(x-1)
# print(func(N)//(func(K)*func(N-K)))
# #print(func(N))
N,K = map(int,input().split())

upper = 1
for i in range(2,N+1) :
    upper*=i
under_1 = 1
for i in range(2,K+1) :
    under_1 *= i
under_2 = 1
for i in range(2,(N-K)+1) :
    under_2 *= i
print(upper//(under_1*under_2))