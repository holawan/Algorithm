import sys

sys.stdin = open("input.txt","r")


for _ in range(1,11) :
    garo = int(input())
    building = list(map(int,input().split()))
    cnt = 0
    for i in range(2,garo-1) :
        if building[i]>building[i-1] and building[i]>building[i-2] and building[i]>building[i+1] and building[i]>building[i+2] :
            lst = [building[i - 2], building[i - 1], building[i + 1]]
            x = building[i+2]
            for build in lst :
                if build> x :
                    x = build
            cnt += building[i] - x
    print(f'#{_} {cnt}')