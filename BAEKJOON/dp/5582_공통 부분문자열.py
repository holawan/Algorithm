S1 = input()
S2 = input()


if len(S1) > len(S2) :
    S1,S2 = S2,S1

res = 0
# print(S1,S2)
x = 1 
for i in range(len(S2)) :
    x=res
    # print(x)
    if i+x >= len(S2) :
        break
    while True :
        tmp_str = S2[i:i+x] 
        if tmp_str in S1 and len(tmp_str) >= res  :
            print(x)
            res = len(tmp_str)
            x += 1 
            # print(tmp_str)
        else :
            break


print(res)