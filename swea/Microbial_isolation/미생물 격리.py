
from collections import defaultdict

t = int(input())
# 상 하 좌 우
# 1  2  3  4
# 상 우 하 좌
# 0  1  2  3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for case in range(t):
    n, m, k = map(int,input().split())
    dic = defaultdict(list)

    for _ in range(k):
        x,y,num,direction = map(int,input().split())
        if direction == 1:
            direction = 0
        elif direction == 4:
            direction = 1
        dic[(x,y)] = [[num,direction]]
    for _ in range(m):
        tmp_dic = defaultdict(list)

        for key,val in dic.items():
            x,y = key
            num, direction = val[0]

            nx = x + dx[direction]
            ny = y + dy[direction]
            if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
                num = num//2
                if num>0:
                    tmp_dic[(nx,ny)].append([num,(direction+2)%4])
            else:
                tmp_dic[(nx,ny)].append([num,direction])

        dic = defaultdict(list)
        for key,val in tmp_dic.items():
            if len(val) == 1:
                dic[key].append(val[0])
            else:
                tmp = 0
                s = 0
                d = 0
                for num,direction in val:
                    if num > tmp:
                        tmp = num
                        d = direction
                    s += num
                dic[key].append([s,d])
    res = sum([x[0][0] for x in dic.values()])

    print(f"#{case+1} {res}")





