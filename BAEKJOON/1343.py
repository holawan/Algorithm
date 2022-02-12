poliomino = input()

poliomino= poliomino.replace('XXXX','AAAA')
poliomino = poliomino.replace('XX','BB')

if 'X' in poliomino:
    print(-1)
else :
    print(poliomino)