lst = ['a','e','i','o','u']
accept = ['ee','oo']
while True :
    x=y=0
    password = input()
    if password == 'end' :
        break
    cnt = 0
    for i in lst :
        if i in password :
            cnt +=1 
    if cnt <1 :
        print(f'<{password}> is not acceptable.')
        continue
    for i in range(len(password)-2) :
        if password[i] in lst and password[i+1] in lst and password[i+2] in lst :
            x = 1 
        elif not(password[i] in lst) and not(password[i+1]in lst) and not(password[i+2] in lst) :
            x = 1 
    if x == 1 :
        print(f'<{password}> is not acceptable.')
        continue

    for i in range(len(password)-1) :
        if password[i]==password[i+1] :
            if password[i] == 'e' or password[i] == 'o' :
                continue
            else :
                y = 1 
    if y == 1 :
        print(f'<{password}> is not acceptable.')
        continue
    print(f'<{password}> is acceptable.')
