#물웅덩이, 널빤지의 길이 
N,L = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort()
# print(lst)
cnt =0  

for pool in range(len(lst)) :
    #웅덩이의 길이 
    length = lst[pool][1]-lst[pool][0]
    #마지막 웅덩이일 경우 
    if pool == len(lst)-1 :
        #index를 맞추기 위해 -1을 추가로 해주고 나눈 값을 더해준다 
        cnt +=  (length-1)//L +1
        break
    #웅덩이 크기를 널빤지로 나눈 값이 맞아 떨어지지 않을 때 
    if (length)% L  :
        #널빤지가 어디까지 갔는지 확인할 tmp 
        tmp = L - ((length)% L)
        #현재 웅덩이 마지막에서 tmp를 더한값만큼 웅덩이 증가 
        now_corver = lst[pool][1] + tmp 
        # print(now_corver,'xx')
        #다음 웅덩이 시작이 현재 웅덩이 시작값보다 작거나 같으면 
        if lst[pool+1][0] <=now_corver : 
            #다음웅덩이 시작을 현재 널빤지 마지막 위치로 
            lst[pool+1][0] = now_corver
        cnt += (length)//L +1
    # 만약 널빤지가 딱 맞는다면 길이를 널빤지 수로 나눈 값을 사용 
    else : 
        cnt += (length)//L 
    # print(lst)



# x= 0 
# lst = []
# for i in range(len(tmp_lst)) :
#     if x == 1 :
#         x = 0
#         continue
#     if i == len(tmp_lst)-1 :
#         lst.append(tmp_lst[i])
#         break
#     if tmp_lst[i][1] +1 == tmp_lst[i+1][0] :
#         new_lst = [tmp_lst[i][0],tmp_lst[i+1][1]]
#         lst.append(new_lst)
#         x = 1 
#     else :
#         lst.append(tmp_lst[i])

# print(lst)



# road = list(0 for _ in range(lst[-1][1]))

# for x in lst : 
#     for _ in range(x[0],x[1]) :
#         road[_] = 1
# print(road)
# cnt =0
# tmp = -1
# for i in range(len(road)) :
#     if i<=tmp :
#         continue
#     if road[i] :
#         for up in range(i,i+3) :
#             road[up] = 0
#         cnt += 1 
#         tmp = up

print(cnt)
