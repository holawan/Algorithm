N = int(input())
score = list(map(int,input().split()))
new_score = []
m = max(score)
for s in score :
    new_score.append(s/m*100)
print(round(sum(new_score)/N,6))

