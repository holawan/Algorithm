import sys 

input = sys.stdin.readline

n = input()

dp = [0 for _ in range(len(n)+1)]
if n[0] == '0' :
    print('0')
#dp[i] = dp[i] + dp[i-1]
#dp[i] = dp[i] + dp[i-2]
else :
    dp[0] = 1 
    dp[1] = 1 

    n = '0'+n

    for i in range(2,len(n)) :

        if n[i] > '0' :
            dp[i] += dp[i-1]

        if n[i-1] != '0' and n[i-1] + n[i] < '27' :
            dp[i] += dp[i-2]
    print(dp[-2]%1000000)