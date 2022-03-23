T  = int(input())
import math
for t in range(1,T+1) :
    n = int(input())

    x = n**(1/3)
    if math.isclose(x, round(x)) :
        print(f'#{t} {round(x)}')
    else :
        print(f'#{t} {-1}')