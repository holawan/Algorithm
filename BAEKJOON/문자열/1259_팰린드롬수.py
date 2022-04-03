while True :
    #0이 나올때까지 받기 
    number = input()
    if number == '0' :
        break
    #뒤집어서 같으면 yes
    if number == number[::-1] :
        print('yes')
    #아니면 no
    else : 
        print('no')