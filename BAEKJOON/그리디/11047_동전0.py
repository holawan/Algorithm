N, K = map(int, input().split()) 
lst = list()
for i in range(N):
    lst.append(int(input()))

cnt = 0
for i in range(N-1,-1,-1):
    cnt += K//lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(cnt)