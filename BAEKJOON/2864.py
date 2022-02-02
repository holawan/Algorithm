lst = list(map(str,input().split()))
new = []
for num in lst :
    for i in num :
        if i == '5' :
            new.append(num.replace('5','6'))
        elif i == '6' :
            new.append(num.replace('6','5'))
