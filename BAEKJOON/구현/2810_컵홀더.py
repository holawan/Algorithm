n = int(input())
s = input()

s = s.replace('LL','X')

if 'X' in s :
    print(len(s)+1)
else :
    print(len(s))
