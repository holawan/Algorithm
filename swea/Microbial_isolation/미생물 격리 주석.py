
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

    # 인풋받기, key : (x, y) / value : (개수, 방향)
    for _ in range(k):
        x,y,num,direction = map(int,input().split())

        # 방향 전환이 쉽도록 값을 바꿔줌
        if direction == 1:
            direction = 0
        elif direction == 4:
            direction = 1

        # 차후에 dic의 value에는 여러개의 (num, direction) 쌍이 들어갈 예정이므로, 여기서도 이중 리스트로 입력을 받음.
        dic[(x,y)] = [[num,direction]]
        
    for _ in range(m):
        # 이동 후 위치를 저장할 딕셔너리를 새로 만들어줌
        tmp_dic = defaultdict(list)

        for key,val in dic.items():
            x,y = key
            # val[0]인 이유는 바로 위의 주석에서 처럼 이중 리스트이기 때문
            num, direction = val[0]

            nx = x + dx[direction]
            ny = y + dy[direction]

            # 벽에 부딪히면 숫자는 반토막 / num = 0이면 사라짐 / 아니면 딕셔너리에 방향 바꿔서 append
            if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
                num = num//2
                if num>0:
                    tmp_dic[(nx,ny)].append([num,(direction+2)%4])

            # 벽에 안부딫히면 x, y만 바꿔서 append
            else:
                tmp_dic[(nx,ny)].append([num,direction])


        # 겹치는 좌표 확인 부분

        dic = defaultdict(list)
        for key,val in tmp_dic.items():

            # value에 값이 1개면 그대로 사용
            if len(val) == 1:
                dic[key].append(val[0])

            # 아니라면 합해줌
            else:
                # tmp : 최대값 / s : 합계 / d : 방향
                tmp = 0
                s = 0
                d = 0
                # 최대값보다 큰 경우만 방향을 바꿔줌. 
                for num,direction in val:
                    if num > tmp:
                        tmp = num
                        d = direction
                    s += num
                dic[key].append([s,d])
    # x : dic의 value, [[num, direction]] / x[0] : [num, direction] / x[0][0] : num
    res = sum([x[0][0] for x in dic.values()])

    print(f"#{case+1} {res}")





