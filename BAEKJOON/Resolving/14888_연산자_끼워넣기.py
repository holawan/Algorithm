from itertools import permutations

def minimum(num,real_sub) :
    global my_min
    for sub in real_sub :
        result = num[0]
        for i in range(N-1) :
            if int(result)<0 and sub[i] == '//' and int(num[i+1])>0 :
                result = -(-int(result)//int(num[i+1]))
            else :
                result = eval(str(result)+sub[i]+num[i+1])

        if result < my_min :
            my_min = result

def maximum(num,real_sub) :
    global my_max
    for sub in real_sub :
        result = num[0]
        for i in range(N-1) :
            if int(result)<0 and sub[i] == '//' and int(num[i+1])>0 :
                result = -(-int(result)//int(num[i+1]))
            else :
                result = eval(str(result)+sub[i]+num[i+1])
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

real_sub = list(permutations(real,len(real)))
# print(real_sub)
my_min = 10e9
my_max = 0
minimum(numbers,real_sub)
maximum(numbers,real_sub)
print(my_max)
print(my_min)




