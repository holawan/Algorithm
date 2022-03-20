T = int(input()) #테스트 케이스
for t in range(1,T+1): #출력형식 맞추기 위해 1부터 T+1 까지
    K,N,M = map(int,input().split()) #이동거리, 정류장 수, 충전기가 설치된 정류장 수
    charge_center = list(map(int,input().split())) # 충전기가 설치된 정류장
    charge = [0] * (N+1) #충전소 위치를 반환할 charge 리스트

    for place in charge_center : #충전기가 있으며 충전소 위치를 입력
        charge[place] +=1
    start = 0 #현위치를 0으로 시작
    charge_num = 0 #충전횟수

    while start < N : #현위치가 마지막 정류장 수 작으면 계속 반복
        if N - start <= K: #마지막 정류장에서 현 위치를 뺀 값이 이동가능 거리보다 작으면
            break #중지
        if not(1 in charge[start+1:start+K+1]) : #현 위치 +1 부터 현위치 + 이동가능 거리 안에 충전소가 없으면
            charge_num =0 #충전횟수를 0으로 반환하고 반복문 중단
            break
        else :
            for j in range(len(charge[start:start+K+1])) : #현 위치에서 이동 가능 거리를 순회하며
                if charge[start:start+K+1][j] == 1 : #충전소가 있으면 n 은 충전소
                    n = j   #마지막 충전소 위치를 반환하기 위해 반복문을 실시
            start += n #현 위치를 다음 충전소로 갱신
            charge_num += 1 #충전횟수 +
    print(f'#{t} {charge_num}')