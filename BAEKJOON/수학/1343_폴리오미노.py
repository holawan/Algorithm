poliomino = input()

#폴리오미노로 덮기 
poliomino= poliomino.replace('XXXX','AAAA')
poliomino = poliomino.replace('XX','BB')

#안덮인 부분이 있으면 -1출력 
if 'X' in poliomino:
    print(-1)
else :
    print(poliomino)