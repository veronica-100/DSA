dp = [[0] * (amount + 1) for _ in range(n + 1) ]
print(dp)
for i in range(n + 1):
    dp[i][0] = 1

print(dp)