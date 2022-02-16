T = int(input())
for t in range(1, T + 1):
    n = int(input())
    car_lst = list(map(int, input().split()))
    max_cnt = cnt = 1
    for i in range(n - 1):
        if car_lst[i + 1] > car_lst[i]:
            cnt += 1
        else:
            cnt = 1
        if cnt > max_cnt:
            max_cnt = cnt
    print(f'#{t} {max_cnt}')