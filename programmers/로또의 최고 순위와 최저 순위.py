def solution(lottos, win_nums):
    
    #0개,1개 꼴등 ,2개 5등,3개4등,4개3등,5개 2등,6개 1등 
    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)    # lottos 안의 0의 개수를 반환
    # 현재 숫자에서 로또 최저 등수 찾기 
    ans = 0
    #정답을 돌면서 정답이 내 번호에 있으면 ans += 1 
    for x in win_nums:
        if x in lottos:
            ans += 1
    #0을 다 맞추면 최고!, 0을 다 못맞추면 최저
    return rank[cnt_0 + ans],rank[ans]