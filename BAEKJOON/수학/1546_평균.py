N = int(input())
#점수를 받아온다. 
score = list(map(int,input().split()))
new_score = []
#평균을 계산할 때 기준이 될 최대값 
m = max(score)
for s in score :
    new_score.append(s/m*100)
print(round(sum(new_score)/N,6))

