N = int(input())
lst = []
for i in range(N) :
    lst.append(list(map(str,input().split())))

for word in lst :
    num = int(word[0])
    for j in word[1]:
        print(num*j,end='')
    print('')