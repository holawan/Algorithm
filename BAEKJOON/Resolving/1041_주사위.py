N = int(input())
dice = list(map(int, input().split()))

if N == 1:
    print(sum(dice)-max(dice))
else:
    lst = [min(dice[0], dice[5]),
               min(dice[1], dice[4]),
               min(dice[2], dice[3])]
    lst.sort()

    n1 = (N-2)*(N-2) + (N-1)*(N-2)*4
    n2 = (N-2)*4 + (N-1)*4
    n3 = 4

    ans = n1 * lst[0] + n2 * sum(lst[:2]) + n3 * sum(lst)
    print(ans)