#이진탐색기 만들기
def binary_search(target) :
    start = 1 #책의 시작 쪽수
    end = Page #끝 쪽수
    cnt = 1 #반복 횟수
    while start<=end : #찾으려는 부분 처음이 끝보다 작거나 같으면
        middle = (start+end)//2 #middle start+end를 2로 나눈 값의 몫
        if target == middle : #target과 middle이 같으면
            return cnt #반복 횟수 반환
        elif middle > target : #middle이 찾으려는 target보다 크면
            end = middle #마지막 부분을 middle로 갱신
        else : #middle이 찾으려는 target보다 작으면
             start = middle #처음 부분을 middle로 갱신
        cnt +=1
    return False

T = int(input())
for t in range(1,T+1) :
    Page,A,B = map(int,input().split())
    if binary_search(A) == False and binary_search(B) == False : #둘다 실패하면 0 반환
        print(f'#{t} 0')
    elif binary_search(A) == False : #A만 실패하면 B 반환
        print(f'#{t} B')
    elif binary_search(B) == False : #B만 실패하면 A 반환
        print(f'#{t} A')
    elif binary_search(A) > binary_search(B) : #cnt가 더 높으면 패배
        print(f'#{t} B')
    elif binary_search(B) > binary_search(A) :
        print(f'#{t} A')
    else :#같으면 0 반환
        print(f'#{t} 0')
