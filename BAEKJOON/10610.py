lst = list(input())
lst.sort(reverse = True)

if lst[-1] != '0':
    print(-1)
    exit()

summ = 0
for number in lst :
    summ += int(number)

if summ %3 != 0 :
    print(-1)
else :
    print(''.join(lst)) 
