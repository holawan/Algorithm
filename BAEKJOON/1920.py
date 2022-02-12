import sys
n = int(sys.stdin.readline())
N_lst = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())


def func(b,d) :
    for num in d :
        for i in b :
            if i == num :
                return 1
    return 0
print()

# for num in list(map(int,sys.stdin.readline().split())) :
#     for i in N_lst : 
#         if i == num :
#             print(1)
#             continue
#     print(0)