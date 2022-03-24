
T = int(input())

for t in range(1,T+1) :
    l,num = input().split()
    l = int(l)
    ans = ''
    num_int = 0
    for i in range(l) :
        if num[i] == 'A' :
            num_int = 10
        elif num[i] == 'B':
            num_int = 11
        elif num[i] == 'C' :
            num_int = 12
        elif num[i] == 'D' :
            num_int = 13
        elif num[i] == 'E' :
            num_int = 14
        elif num[i] == 'F' :
            num_int = 15
        else :
            num_int = int(num[i])

        binary_num = ['0']*4
        i = 3
        while num_int >0  :
            binary_num[i] = str(num_int%2)
            num_int = num_int//2 
            i -= 1 
        ans += ''.join(binary_num)
    print(f'#{t} {ans}')

