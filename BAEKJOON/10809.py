S = input()
alphabet= 'abcdefghijklmnopqrstuvwxyz'

for word in alphabet :
    if word in S :
        print(S.index(word),end=' ')
    else :
        print(-1,end=' ')
        
