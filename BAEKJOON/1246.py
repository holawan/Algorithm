# N,M = map(int,input().split())
# lst = [int(input()) for i in range(M)]

# S = 0

# for i in range(min(lst),max(lst)+1):
#     x = 0
#     for j in lst:
#         if i <= j :
#             x += 1
#     if x*i >S :
#         S = x*i
#         price = i

# print(price,S)


import sys
N,M = map(int,sys.stdin.readline().split())
lst = [int(sys.stdin.readline()) for i in range(M)]

#초기 수익 0원, 가격 0원
S = 0
price = 0
#구매희망자 리스트 오름차순 정렬
lst.sort()
for i in lst :
    #판매가능한 계란수가 값이 가지고 있는 계란수보다 크면 continue
    #M-lst.index(i) 는 구매 희망자에서 판매 계란을 뺀 값 = 판매가능한 계란
    if (M-lst.index(i)) > N :
        continue
    #x는 가격 * 판매가능 계란
    x = i*(M-lst.index(i))
    if x>S :
        S = x
        price = i
print(price,S)