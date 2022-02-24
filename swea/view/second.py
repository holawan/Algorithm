import sys
sys.stdin = open('input.txt','r')

for t in range(1,11) :
    n = int(input())
    buildings = list(map(int,input().split()))
    result = 0
    for x in range(2,n-2) :
        cnt = -1
        calculator = [buildings[x-2],buildings[x-1],buildings[x+1],buildings[x+2]]
        for building in calculator :
            if buildings[x] <= building :
                cnt = 0
                continue
        if cnt == 0 :
            continue
        else :
            result += buildings[x] - max(calculator)
    print(f'#{t} {result}')


