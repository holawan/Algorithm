import sys
from itertools import permutations


N = int(sys.stdin.readline())  # 이닝 수
ining_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

people = [x for x in range(1,9)]

answer = 0

for turn in permutations(people, 8):

    turn = list(turn[:3]) + [0] + list(turn[3:])
    # print(turn) 

    score = 0
    index = 0
    for now in range(N):
        out = 0  # 아웃 카운트
        b_1, b_2, b_3 = 0, 0, 0  # 1, 2, 3루 주자
        while out < 3:
            if ining_lst[now][turn[index]] == 0:
                out += 1
            elif ining_lst[now][turn[index]] == 1:
                score += b_3
                b_1, b_2, b_3 = 1, b_1, b_2
            elif ining_lst[now][turn[index]] == 2:
                score += (b_2 + b_3)
                b_1, b_2, b_3 = 0, 1, b_1
            elif ining_lst[now][turn[index]] == 3:
                score += (b_1 + b_2 + b_3)
                b_1, b_2, b_3 = 0, 0, 1
            elif ining_lst[now][turn[index]] == 4:
                score += (b_1 + b_2 + b_3 + 1)
                b_1, b_2, b_3 = 0, 0, 0
            
            index =(index+1)%9

    answer = max(answer, score)
print(answer)