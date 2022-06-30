# 랜선의 수, 필요한 랜선 수 
K,N = map(int,input().split())

#영식이가 가지고 있는 랜선 가져오기 
lst = [int(input()) for _ in range(K)]

#최소 랜선 길이는 1 
start = 1 
#최대 랜선 길이는 모든 랜선을 11로 나눴을 때 
end = int(sum(lst)/N)

#최소랜선이 최대 랜선보다 작으면 이분탐색 
while start <= end : 
    #중간지점은 start+end 합을 2로 나눈 몫 
    middle = (start+end)// 2 

    #랜선 구해보기 
    tmp = 0

    #랜선을 돌면서 현재 값으로 잘라보기 
    for k in lst :
        tmp += k//middle 
    #자른게 요구되는 것보다 크거나 같으면 start를 middle+1로 줘서 더 커질 수 있는지 확인 
    if tmp >= N :
        start = middle + 1 
    #자른게 요구된것보다 작으면 end를 middle-1로  낮추기 
    else :
        end = middle -1 
print(end)