n = int(input())
num_lst = list(map(int,input().split()))

answer = [-1]*n 

 
stack = [0]

for i in range(1,n) :
    while stack and num_lst[stack[-1]] < num_lst[i] :
        answer[stack.pop()] = num_lst[i]
    stack.append(i)

print(*answer)