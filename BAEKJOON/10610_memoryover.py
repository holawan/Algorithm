from itertools import permutations

num = input()
if not('0' in num) :
    print(-1)
    exit()
lst = list(i for i in num)
combi = list(permutations(lst,len(num)))
lst2 = []
result = []
for numbers in combi:
    numbers = list(numbers)
    x = ''
    for string in numbers :
        x += string
    if int(x)%30 == 0:
        result.append(int(x))
    #lst2.append(int(x))

result.sort()
if result == [] :
    print(-1)
else :
    print(result[-1])

